from dataclasses import dataclass

from rag_juridico.domain.entities.evidence import Evidence


@dataclass(frozen=True, slots=True)
class Answer:
    content: str
    evidence: tuple[Evidence, ...]
    insufficient_evidence: bool = False
