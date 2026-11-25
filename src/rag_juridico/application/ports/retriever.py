from typing import Protocol

from rag_juridico.domain.entities.evidence import Evidence


class Retriever(Protocol):
    async def retrieve(
        self,
        query: str,
        *,
        limit: int = 5,
    ) -> list[Evidence]:
    ...
