from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv
import uvicorn

from app.rag_service import RAGService
from app.document_processor import DocumentProcessor

load_dotenv()

app = FastAPI(title="RAG Document Q&A API")

# CORS middleware to allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # React dev servers
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
rag_service = RAGService()
doc_processor = DocumentProcessor()

class QuestionRequest(BaseModel):
    question: str
    chat_history: Optional[List[dict]] = []

class QuestionResponse(BaseModel):
    answer: str
    sources: Optional[List[str]] = []

@app.get("/")
async def root():
    return {"message": "RAG Document Q&A API", "status": "running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """Upload and process a document"""
    try:
        # Save uploaded file temporarily
        file_path = f"/tmp/{file.filename}"
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        
        # Process document
        result = await doc_processor.process_document(file_path, file.filename)
        
        # Clean up temp file
        os.remove(file_path)
        
        return {
            "message": "Document processed successfully",
            "filename": file.filename,
            "chunks": result.get("chunks", 0)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ask", response_model=QuestionResponse)
async def ask_question(request: QuestionRequest):
    """Ask a question using RAG"""
    try:
        result = await rag_service.ask_question(
            question=request.question,
            chat_history=request.chat_history
        )
        return QuestionResponse(
            answer=result["answer"],
            sources=result.get("sources", [])
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/clear")
async def clear_documents():
    """Clear all documents from the vector database"""
    try:
        await doc_processor.clear_database()
        return {"message": "Database cleared successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
