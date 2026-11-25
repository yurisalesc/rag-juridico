from typing import Protocol

from rag_juridico.domain.entities.evidence import Evidence


class LanguageModel(Protocol):
    async def generate(
        self,
        question: str,
        evidence: list[Evidence],
    ) -> str: ...
