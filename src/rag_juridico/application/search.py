from rag_juridico.application.ports import Retriever
from rag_juridico.domain.evidence import Evidence


class SearchDocuments:
    def __init__(self, retriever: Retriever, default_limit: int = 5) -> None:
        self._retriever = retriever
        self._default_limit = default_limit

    def execute(self, query: str, *, limit: int | None = None) -> list[Evidence]:
        query = query.strip()
        if not query:
            raise ValueError("Query cannot be empty.")
        effective_limit = self._default_limit if limit is None else limit
        if not 1 <= effective_limit <= 50:
            raise ValueError("Invalid retrieval limit. It must be between 1 and 50.")
        return self._retriever.retrieve(query, limit=effective_limit)
