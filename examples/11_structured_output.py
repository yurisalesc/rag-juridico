from typing import Literal

from pydantic import BaseModel, Field

from rag_juridico.bootstrap.models import build_chat_model
from rag_juridico.bootstrap.settings import Settings


class LegalClassification(BaseModel):
    area: Literal["civil", "penal", "trabalhista", "tributario", "outros"]
    requires_research: bool
    keywords: list[str] = Field(description="Termos de pesquisa jurídica")


def main() -> None:
    model = build_chat_model(Settings()).with_structured_output(
        LegalClassification,
        method="json_schema",
    )
    result = model.invoke("Quais os requisitos para indenização por dano moral?")
    if not isinstance(result, LegalClassification):
        raise RuntimeError("Unexpected response schema.")
    print(result.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
