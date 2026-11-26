from dataclasses import dataclass

from rag_juridico.domain.evidence import Evidence


@dataclass(frozen=True, slots=True)
class DraftAnswer:
    content: str
    citations_ids: tuple[str, ...]
    sufficient_evidence: bool
