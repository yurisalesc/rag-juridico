from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

from rag_juridico.domain.evidence import Evidence


class QdrantEvidenceStore:
    def __init__(
        self, client: QdrantClient, embeddings: Embeddings, collection_name: str
    ) -> None:
        if not client.collection_exists(collection_name):
            dimensions = len(embeddings.embed_query("dimension check"))
            client.create_collection(
                collection_name=collection_name,
                vectors_config=VectorParams(
                    size=dimensions,
                    distance=Distance.COSINE,
                ),
            )
            self._store = QdrantVectorStore(
                client=client,
                collection_name=collection_name,
                embeddings=embeddings,
            )

    def upsert(self, evidence: list[Evidence]) -> None:
        if not evidence:
            return
        documents = [
            Document(
                page_content=item.content,
                metadata={
                    "evidence_id": item.id,
                    "source": item.source,
                    "page": item.page,
                },
            )
            for item in evidence
        ]
        self._store.add_documents(
            documents=documents, ids=[str(item.id) for item in evidence]
        )

    def retrieve(self, query: str, *, limit: int) -> list[Evidence]:
        return [
            Evidence(
                id=doc.metadata["evidence_id"],
                source=doc.metadata["source"],
                content=doc.page_content,
                page=doc.metadata.get("page"),
            )
            for doc in self._store.similarity_search(query, k=limit)
        ]
