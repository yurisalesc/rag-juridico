import asyncio

from langchain_core.messages import HumanMessage, SystemMessage

from rag_juridico.bootstrap.models import build_chat_model
from rag_juridico.bootstrap.settings import Settings


async def main() -> None:
    model = build_chat_model(Settings())
    messages = [
        SystemMessage(content="Responda em português e de forma concisa."),
        HumanMessage(content="Qual a diferença entre dano moral e material?"),
    ]

    async with asyncio.timeout(180):
        response = await model.ainvoke(messages)
    print(response.text)


if __name__ == "__main__":
    asyncio.run(main())
