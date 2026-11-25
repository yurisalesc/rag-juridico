from rag_juridico.application.dto.answer import Answer
from rag_juridico.application.ports.retriever import Retriever
from rag_juridico.application.ports.language_model import LanguageModel


class AnswerQuestion:
    def __init__(
        self,
        retriever: Retriever,
        language_model: LanguageModel,
    ) -> None:
        self._retriever = retriever
        self._language_model = language_model

    async def execute(self, question: str) -> Answer:
        question = question.strip()
        if not question:
            raise ValueError("Question cannot be empty.")

        evidence = await self._retriever.retrieve(question)
        if not evidence:
            return Answer(
                content="Insufficient evidences.",
                evidence=(),
                insufficient_evidence=True,
            )

        response = await self._language_model.generate(
            question=question,
            evidence=evidence,
        )

        return Answer(
            content=response,
            evidence=tuple(evidence),
        )
