from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class LegalDocument:
    source: str
    content: str
    page: int | None = None
