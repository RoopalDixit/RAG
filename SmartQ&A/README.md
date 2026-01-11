# RAG Document Q&A Application

A full-stack RAG (Retrieval-Augmented Generation) application with document upload and Q&A capabilities using LangChain, ChromaDB, and React.

## Features

- 📄 **Document Upload**: Support for PDF, TXT, DOCX, CSV, and Markdown files
- 🔍 **Vector Search**: ChromaDB for efficient document retrieval
- 🤖 **Multiple LLM Support**: OpenAI (GPT) and Anthropic (Claude) APIs
- 💬 **Interactive Chat**: Conversational Q&A interface with chat history
- ⚡ **Fast API Backend**: FastAPI with async support
- 🎨 **Modern React Frontend**: Beautiful, responsive UI

## Architecture

```
rag-app/
├── backend/          # FastAPI backend
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py          # Configuration management
│   │   ├── document_processor.py  # Document processing & ChromaDB
│   │   ├── llm_factory.py     # LLM initialization (OpenAI/Claude)
│   │   └── rag_service.py     # RAG chain implementation
│   ├── main.py                # FastAPI application
│   ├── requirements.txt
│   └── .env.example
└── frontend/        # React frontend
    ├── src/
    │   ├── components/
    │   │   ├── DocumentUpload.jsx
    │   │   └── ChatInterface.jsx
    │   ├── App.jsx
    │   └── main.jsx
    └── package.json
```

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
```bash
cd rag-app/backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file from the example:
```bash
cp .env.example .env
```

5. Edit `.env` and add your API keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
DEFAULT_PROVIDER=openai  # or "claude"
```

6. Run the backend server:
```bash
python main.py
# Or: uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd rag-app/frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

## Usage

1. **Start the backend server** (port 8000)
2. **Start the frontend server** (port 3000)
3. **Upload documents** using the upload button
4. **Ask questions** about your uploaded documents in the chat interface

## API Endpoints

- `GET /` - API status
- `GET /health` - Health check
- `POST /upload` - Upload and process a document
- `POST /ask` - Ask a question (requires JSON body with `question` and optional `chat_history`)
- `DELETE /clear` - Clear all documents from the database

## Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required for embeddings)
- `ANTHROPIC_API_KEY`: Your Anthropic API key (optional, for Claude)
- `DEFAULT_PROVIDER`: Either "openai" or "claude" (default: "openai")
- `OPENAI_MODEL`: OpenAI model name (default: "gpt-4o-mini")
- `CLAUDE_MODEL`: Claude model name (default: "claude-3-5-sonnet-20241022")
- `EMBEDDING_MODEL`: Embedding model (default: "text-embedding-3-small")
- `CHUNK_SIZE`: Document chunk size (default: 1000)
- `CHUNK_OVERLAP`: Chunk overlap (default: 200)
- `CHROMA_DB_PATH`: Path to ChromaDB storage (default: "./chroma_db")

## Supported File Formats

- PDF (`.pdf`)
- Text files (`.txt`)
- Markdown (`.md`)
- Word documents (`.docx`, `.doc`)
- CSV files (`.csv`)

## Technologies Used

### Backend
- FastAPI - Modern Python web framework
- LangChain - LLM application framework
- ChromaDB - Vector database
- OpenAI/Anthropic APIs - LLM providers

### Frontend
- React 18 - UI library
- Vite - Build tool
- Axios - HTTP client

## License

MIT
