# RAG Projects Repository

A comprehensive collection of Retrieval-Augmented Generation (RAG) projects and learning materials, including educational notebooks on LangSmith observability and a production-ready full-stack RAG application.

## 📚 Repository Overview

This repository contains two main projects:

1. **RAG Tracing** - Educational project from LangSmith Academy focusing on observability, tracing, and evaluation of RAG applications
2. **SmartQ&A** - Production-ready full-stack RAG application with document upload, vector search, and conversational Q&A

---

## 🎯 Projects

### 1. RAG Tracing (LangSmith Academy)

**Educational Project | Learning LangSmith Observability**

A comprehensive tutorial project exploring LangSmith's capabilities for tracing, evaluating, and monitoring RAG applications. This project includes modules covering the fundamentals of observability, prompt engineering, evaluations, and production monitoring.

#### Key Features:
- 📊 **Tracing Basics**: Learn to trace LLM applications with the `@traceable` decorator
- 🧵 **Conversational Threads**: Track multi-turn conversations in chatbot interfaces
- 🔍 **Evaluation Systems**: Implement evaluators for RAG applications
- 📈 **Experiments & Datasets**: Run experiments and manage datasets
- 🎨 **Prompt Engineering**: Explore prompt engineering lifecycle and Prompt Hub
- 📝 **Feedback Mechanisms**: Implement feedback collection and publishing
- 🔬 **Production Monitoring**: Set up filtering and online evaluation

#### Module Structure:
- **Module 0**: RAG Application Basics
- **Module 1**: Tracing Basics, Alternative Tracing Methods, Conversational Threads, Types of Runs
- **Module 2**: Evaluators, Experiments, Dataset Upload, Pairwise Experiments
- **Module 3**: Prompt Engineering Lifecycle, Playground Experiments, Prompt Hub
- **Module 4**: Publishing Feedback
- **Module 5**: Filtering, Online Evaluation

#### Technologies:
- LangChain / LangGraph
- LangSmith (Observability Platform)
- OpenAI API
- Jupyter Notebooks
- scikit-learn (for vector store)

#### Quick Start:
```bash
cd "RAG Tracing"
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Set up environment variables in .env:
# OPENAI_API_KEY=your_key
# LANGSMITH_API_KEY=your_key
# LANGSMITH_TRACING=true
# LANGSMITH_PROJECT=langsmith-academy
```

For detailed setup instructions, see [RAG Tracing/README.md](RAG%20Tracing/README.md)

---

### 2. SmartQ&A (Full-Stack RAG Application)

**Production Application | Document Q&A System**

A complete full-stack RAG application that enables users to upload documents and query them using natural language. Built with FastAPI backend, React frontend, and ChromaDB for vector storage.

#### Key Features:
- 📄 **Multi-Format Document Upload**: Support for PDF, TXT, DOCX, CSV, and Markdown files
- 🔍 **Vector Search**: ChromaDB for efficient semantic document retrieval
- 🤖 **Multiple LLM Support**: OpenAI (GPT-4) and Anthropic (Claude) APIs
- 💬 **Conversational Interface**: Interactive chat with conversation history
- ⚡ **Fast API Backend**: FastAPI with async support
- 🎨 **Modern React Frontend**: Responsive UI with real-time document upload and Q&A

#### Architecture:
```
SmartQ&A/
├── backend/          # FastAPI backend
│   ├── app/
│   │   ├── config.py          # Configuration management
│   │   ├── document_processor.py  # Document processing & ChromaDB
│   │   ├── llm_factory.py     # LLM initialization (OpenAI/Claude)
│   │   └── rag_service.py     # RAG chain implementation
│   ├── main.py                # FastAPI application
│   └── requirements.txt
└── frontend/        # React frontend
    ├── src/
    │   ├── components/
    │   │   ├── DocumentUpload.jsx
    │   │   └── ChatInterface.jsx
    │   └── App.jsx
    └── package.json
```

#### Technologies:
- **Backend**: FastAPI, LangChain, ChromaDB, Python
- **Frontend**: React 18, Vite, Axios
- **AI/ML**: OpenAI API, Anthropic API, Vector Embeddings
- **Database**: ChromaDB (Vector Database)

#### Quick Start:
```bash
# Backend Setup
cd SmartQ&A/backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp env.example .env
# Edit .env with your API keys
python main.py  # Runs on http://localhost:8000

# Frontend Setup (in new terminal)
cd SmartQ&A/frontend
npm install
npm run dev  # Runs on http://localhost:3000
```

For detailed setup instructions, see [SmartQ&A/README.md](SmartQ&A/README.md)

---

## 🔄 Project Comparison

| Feature | RAG Tracing | SmartQ&A |
|---------|------------|----------|
| **Purpose** | Educational / Learning | Production Application |
| **Focus** | Observability & Tracing | Document Q&A System |
| **Interface** | Jupyter Notebooks | Web Application (React) |
| **Vector DB** | scikit-learn (SKLearnVectorStore) | ChromaDB |
| **Backend** | Python Scripts | FastAPI |
| **Frontend** | None | React |
| **LLM Providers** | OpenAI | OpenAI + Anthropic |
| **Key Learning** | LangSmith, Tracing, Evaluation | Full-Stack Development, RAG Implementation |

---

## 🚀 Use Cases

### When to Use RAG Tracing:
- Learning LangSmith observability features
- Understanding how to trace and debug LLM applications
- Setting up evaluation systems for RAG
- Exploring prompt engineering workflows
- Learning about production monitoring

### When to Use SmartQ&A:
- Building a document Q&A application
- Creating a production-ready RAG system
- Implementing document upload and processing
- Developing a full-stack AI application
- Need a web interface for RAG

---

## 📋 Prerequisites

### Common Requirements:
- Python 3.11+ (for RAG Tracing)
- Python 3.9+ (for SmartQ&A)
- OpenAI API Key (required for both)
- Node.js 16+ and npm (for SmartQ&A frontend)

### Additional Requirements:
- **RAG Tracing**: LangSmith account and API key
- **SmartQ&A**: Anthropic API key (optional, for Claude support)

---

## 🛠️ Technologies Overview

### Shared Technologies:
- **LangChain**: LLM application framework
- **OpenAI API**: LLM and embedding models
- **Python**: Primary programming language

### RAG Tracing Specific:
- **LangSmith**: Observability and tracing platform
- **LangGraph**: State machine framework
- **Jupyter Notebooks**: Interactive development
- **scikit-learn**: Vector storage

### SmartQ&A Specific:
- **FastAPI**: Modern Python web framework
- **React**: Frontend UI library
- **ChromaDB**: Vector database
- **Anthropic API**: Claude LLM support
- **Vite**: Frontend build tool

---

## 📁 Repository Structure

```
RAG/
├── README.md                    # This file
│
├── RAG Tracing/                 # LangSmith Academy project
│   ├── notebooks/
│   │   ├── module_0/           # RAG Application Basics
│   │   ├── module_1/           # Tracing Basics
│   │   ├── module_2/           # Evaluators & Experiments
│   │   ├── module_3/           # Prompt Engineering
│   │   ├── module_4/           # Feedback Publishing
│   │   └── module_5/           # Filtering & Online Evaluation
│   ├── requirements.txt
│   └── README.md
│
└── SmartQ&A/                    # Full-stack RAG application
    ├── backend/                 # FastAPI backend
    │   ├── app/
    │   ├── main.py
    │   └── requirements.txt
    ├── frontend/                # React frontend
    │   ├── src/
    │   └── package.json
    └── README.md
```

---

## 🎓 Learning Path

### Recommended Learning Order:

1. **Start with RAG Tracing** (if new to LangSmith)
   - Module 0: Understand basic RAG concepts
   - Module 1: Learn tracing fundamentals
   - Module 2: Explore evaluation methods
   - Module 3: Practice prompt engineering

2. **Then explore SmartQ&A** (to see production implementation)
   - Review the architecture
   - Understand the document processing pipeline
   - Explore the RAG service implementation
   - Study the frontend integration

3. **Combine learnings**
   - Apply LangSmith tracing to SmartQ&A
   - Implement evaluation systems
   - Add monitoring and feedback collection

---

## 🔗 Resources

- [LangSmith Documentation](https://docs.smith.langchain.com/)
- [LangChain Documentation](https://python.langchain.com/)
- [ChromaDB Documentation](https://www.trychroma.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)

---

## 📝 Notes

- **RAG Tracing** uses the LangSmith documentation as its data source
- **SmartQ&A** supports user-uploaded documents
- Both projects can be extended and customized
- The projects demonstrate different approaches to RAG implementation

---

## 🤝 Contributing

This is a personal learning repository. Feel free to fork and customize for your own projects!

---

## 📄 License

Both projects in this repository use MIT License (check individual project READMEs for details).

---

## 🎯 Quick Links

- [RAG Tracing Setup Guide](RAG%20Tracing/README.md)
- [SmartQ&A Setup Guide](SmartQ&A/README.md)
- [SmartQ&A API Documentation](SmartQ&A/README.md#api-endpoints)