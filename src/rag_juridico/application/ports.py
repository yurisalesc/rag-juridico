from pathlib import Path
from typing import Protocol

from rag_juridico.domain.evidence import Evidence
from rag_juridico.domain.legal_document import LegalDocument
from rag_juridico.application.dto.answer import Answer
from rag_juridico.application.dto.draft_answer import DraftAnswer


class DocumentLoader(Protocol):
    def load(self, path: Path) -> list[LegalDocument]: ...


class Chunker(Protocol):
    def split(self, documents: list[LegalDocument]) -> list[Evidence]: ...


class EvidenceWriter(Protocol):
    def upsert(self, evidence: list[Evidence]) -> None: ...


class Retriever(Protocol):
    def retrieve(self, query: str, *, limit: int) -> list[Evidence]: ...


class AnswerGenerator(Protocol):
    def generate(self, question: str, evidence: list[Evidence]) -> DraftAnswer: ...


class QueryRetriever(Protocol):
    def rewrite(self, question: str, previous_query: str) -> str: ...


class QuestionAnswerer(Protocol):
    def execute(self, question: str) -> Answer: ...
