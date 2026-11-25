from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Evidence:
    id: str
    content: str
    source: str
    page: int | None = None
    article: str | None = None

    def __post_init__(self) -> None:
        if not self.id.strip():
            raise ValueError("Evidence ID is required.")

        if not self.content.strip():
            raise ValueError("Evidence cannot be empty.")

        if not self.source.strip():
            raise ValueError("Source is required.")
