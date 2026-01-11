from typing import List, Dict, Optional
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

from app.config import Config
from app.document_processor import DocumentProcessor
from app.llm_factory import get_llm

class RAGService:
    def __init__(self):
        self.doc_processor = DocumentProcessor()
        self.llm = get_llm(Config.DEFAULT_PROVIDER)
    
    async def ask_question(
        self,
        question: str,
        chat_history: Optional[List[Dict]] = None,
        provider: Optional[str] = None
    ) -> Dict:
        """Ask a question using RAG"""
        try:
            # Update LLM if provider is specified
            if provider:
                self.llm = get_llm(provider)
            
            # Get retriever
            retriever = self.doc_processor.get_retriever(k=4)
            
            # Convert chat history format
            memory = ConversationBufferMemory(
                memory_key="chat_history",
                return_messages=True,
                output_key="answer"
            )
            
            if chat_history:
                for entry in chat_history:
                    if "human" in entry:
                        memory.chat_memory.add_user_message(entry["human"])
                    if "ai" in entry:
                        memory.chat_memory.add_ai_message(entry["ai"])
            
            # Create conversational retrieval chain
            qa_chain = ConversationalRetrievalChain.from_llm(
                llm=self.llm,
                retriever=retriever,
                memory=memory,
                return_source_documents=True,
                verbose=False
            )
            
            # Get answer
            result = await qa_chain.ainvoke({"question": question})
            
            # Extract sources
            sources = []
            if "source_documents" in result:
                seen_sources = set()
                for doc in result["source_documents"]:
                    source = doc.metadata.get("source", "Unknown")
                    if source not in seen_sources:
                        sources.append(source)
                        seen_sources.add(source)
            
            return {
                "answer": result["answer"],
                "sources": sources
            }
        except Exception as e:
            raise Exception(f"Error processing question: {str(e)}")
