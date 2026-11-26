import asyncio

from rag_juridico.bootstrap.models import build_chat_model
from rag_juridico.bootstrap.settings import Settings


async def main() -> None:
    model = build_chat_model(Settings())
    semaphore = asyncio.Semaphore(2)

    async def explain(question: str) -> str:
        async with semaphore, asyncio.timeout(180):
            response = await model.ainvoke(question)
            return response.text

    questions = ["O que é prescrição?", "O que é decadência?", "O que é mora?"]
    answers = await asyncio.gather(*(explain(q) for q in questions))
    for question, answer in zip(questions, answers, strict=True):
        print(f"Q: {question}\nA: {answer}\n")


if __name__ == "__main__":
    asyncio.run(main())
