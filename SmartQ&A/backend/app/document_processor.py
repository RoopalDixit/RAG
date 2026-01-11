import os
from typing import Dict
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader,
    CSVLoader
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

from app.config import Config
from app.llm_factory import get_embeddings

class DocumentProcessor:
    def __init__(self):
        self.chunk_size = Config.CHUNK_SIZE
        self.chunk_overlap = Config.CHUNK_OVERLAP
        self.embeddings = get_embeddings()
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
        )
        self.vectorstore = self._get_or_create_vectorstore()
    
    def _get_or_create_vectorstore(self):
        """Get or create ChromaDB vectorstore"""
        try:
            # Try to load existing vectorstore
            if os.path.exists(Config.CHROMA_DB_PATH):
                return Chroma(
                    persist_directory=Config.CHROMA_DB_PATH,
                    embedding_function=self.embeddings,
                    collection_name=Config.COLLECTION_NAME
                )
            else:
                # Create new vectorstore
                return Chroma(
                    persist_directory=Config.CHROMA_DB_PATH,
                    embedding_function=self.embeddings,
                    collection_name=Config.COLLECTION_NAME
                )
        except Exception as e:
            print(f"Error creating vectorstore: {e}")
            # Create new one if there's an error
            return Chroma(
                persist_directory=Config.CHROMA_DB_PATH,
                embedding_function=self.embeddings,
                collection_name=Config.COLLECTION_NAME
            )
    
    async def process_document(self, file_path: str, filename: str) -> Dict:
        """Process a document and add it to the vectorstore"""
        try:
            # Load document based on file extension
            file_ext = os.path.splitext(filename)[1].lower()
            
            if file_ext == ".pdf":
                loader = PyPDFLoader(file_path)
            elif file_ext in [".txt", ".md"]:
                loader = TextLoader(file_path, encoding="utf-8")
            elif file_ext in [".docx", ".doc"]:
                loader = Docx2txtLoader(file_path)
            elif file_ext == ".csv":
                loader = CSVLoader(file_path)
            else:
                raise ValueError(f"Unsupported file type: {file_ext}")
            
            documents = loader.load()
            
            # Add metadata
            for doc in documents:
                doc.metadata["source"] = filename
                doc.metadata["file_path"] = file_path
            
            # Split documents into chunks
            chunks = self.text_splitter.split_documents(documents)
            
            # Add to vectorstore
            self.vectorstore.add_documents(chunks)
            
            # Persist the vectorstore
            self.vectorstore.persist()
            
            return {
                "chunks": len(chunks),
                "documents": len(documents)
            }
        except Exception as e:
            raise Exception(f"Error processing document: {str(e)}")
    
    async def clear_database(self):
        """Clear all documents from the vectorstore"""
        try:
            # Delete the collection
            import shutil
            if os.path.exists(Config.CHROMA_DB_PATH):
                shutil.rmtree(Config.CHROMA_DB_PATH)
            
            # Recreate vectorstore
            self.vectorstore = self._get_or_create_vectorstore()
            return True
        except Exception as e:
            raise Exception(f"Error clearing database: {str(e)}")
    
    def get_retriever(self, k: int = 4):
        """Get a retriever from the vectorstore"""
        return self.vectorstore.as_retriever(search_kwargs={"k": k})
