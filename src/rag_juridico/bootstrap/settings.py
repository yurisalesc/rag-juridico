from typing import Self

from pydantic import Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    ollama_base_url: str = "http://localhost:11434"
    ollama_chat_model: str = "qwen2.5:7b"
    ollama_embedding_model: str = "bge-m3"

    qdrant_url: str = "http://localhost:6333"
    qdrant_collection: str = "legal_documents_v1"

    retrieval_top_k: int = Field(default=5, ge=1, le=50)
    chunk_size: int = Field(default=1000, gt=0)
    chunk_overlap: int = Field(default=150, ge=0)

    mcp_url: str = "http://localhost:8001/mcp"

    @model_validator(mode="after")
    def validate_chunking(self) -> Self:
        if self.chunk_overlap >= self.chunk_size:
            raise ValueError("Chunk overlap must be smaller than chunk size.")
        return self
