from qdrant_client import QdrantClient

from rag_juridico.application.ingestion import IngestDocuments
from rag_juridico.application.search import SearchDocuments
from rag_juridico.bootstrap.models import build_embeddings
from rag_juridico.bootstrap.settings import Settings
from rag_juridico.infrastructure.chunking import RecursiveChunker
from rag_juridico.infrastructure.loaders import LocalDocumentLoader
from rag_juridico.infrastructure.qdrant_store import QdrantEvidenceStore


def build_store(settings: Settings) -> QdrantEvidenceStore:
    return QdrantEvidenceStore(
        client=QdrantClient(url=settings.qdrant_url, timeout=30),
        embeddings=build_embeddings(settings),
        collection_name=settings.qdrant_collection,
    )


def build_ingestion(settings: Settings) -> IngestDocuments:
    return IngestDocuments(
        loader=LocalDocumentLoader(),
        chunker=RecursiveChunker(settings.chunk_size, settings.chunk_overlap),
        writer=build_store(settings),
    )


def build_search(settings: Settings) -> SearchDocuments:
    return SearchDocuments(
        retriever=build_store(settings),
        default_limit=settings.retrieval_top_k,
    )
