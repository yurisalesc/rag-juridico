from langchain_ollama import ChatOllama, OllamaEmbeddings

from rag_juridico.bootstrap.settings import Settings


def build_chat_model(settings: Settings) -> ChatOllama:
    return ChatOllama(
        model=settings.ollama_chat_model,
        base_url=settings.ollama_base_url,
        temperature=0,
        num_ctx=8192,
    )


def build_embeddings(settings: Settings) -> OllamaEmbeddings:
    return OllamaEmbeddings(
        model=settings.ollama_embedding_model,
        base_url=settings.ollama_base_url,
    )
