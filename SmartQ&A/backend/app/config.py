import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
    
    # Model Configuration
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-3-5-sonnet-20241022")
    
    # Default provider: "openai" or "claude"
    DEFAULT_PROVIDER = os.getenv("DEFAULT_PROVIDER", "openai")
    
    # ChromaDB Configuration
    CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "./chroma_db")
    COLLECTION_NAME = os.getenv("COLLECTION_NAME", "documents")
    
    # Embedding Configuration
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
    
    # Chunking Configuration
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1000))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 200))
