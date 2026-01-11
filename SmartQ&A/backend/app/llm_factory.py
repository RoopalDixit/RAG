from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_anthropic import ChatAnthropic

from app.config import Config

def get_llm(provider: str = None):
    """Get LLM instance based on provider"""
    provider = provider or Config.DEFAULT_PROVIDER
    
    if provider == "openai":
        if not Config.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY not set in environment variables")
        return ChatOpenAI(
            model=Config.OPENAI_MODEL,
            temperature=0,
            api_key=Config.OPENAI_API_KEY
        )
    elif provider == "claude":
        if not Config.ANTHROPIC_API_KEY:
            raise ValueError("ANTHROPIC_API_KEY not set in environment variables")
        return ChatAnthropic(
            model=Config.CLAUDE_MODEL,
            temperature=0,
            api_key=Config.ANTHROPIC_API_KEY
        )
    else:
        raise ValueError(f"Unsupported provider: {provider}. Use 'openai' or 'claude'")

def get_embeddings():
    """Get embeddings instance"""
    if not Config.OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY not set in environment variables (required for embeddings)")
    return OpenAIEmbeddings(
        model=Config.EMBEDDING_MODEL,
        api_key=Config.OPENAI_API_KEY
    )
