from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Evidence:
    id: str
    source: str
    content: str
    page: int | None = None

    def __post_init__(self) -> None:
        if not all(value.strip() for value in (self.id, self.source, self.content)):
            raise ValueError("Evidence requires id, source, and content.")
        if self.page is not None and self.page < 1:
            raise ValueError("Page number must be positive.")
