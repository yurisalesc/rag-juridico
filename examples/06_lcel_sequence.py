import asyncio

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from rag_juridico.bootstrap.models import build_chat_model
from rag_juridico.bootstrap.settings import Settings


async def main() -> None:
    model = build_chat_model(Settings())
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Explique conceitos de {area} em português, sem inventar fontes.",
            ),
            ("human", "{question}"),
        ]
    )
    chain = prompt | model | StrOutputParser()
    data = {"area": "Direito Civil", "question": "O que é mora?"}

    print("Resposta async:", await chain.ainvoke(data))

    print("Streaming da mesma chain (nova chamada):")
    async for text in chain.astream(data):
        print(text, end="", flush=True)
    print()


if __name__ == "__main__":
    asyncio.run(main())
