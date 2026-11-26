import asyncio

from rag_juridico.bootstrap.models import build_chat_model
from rag_juridico.bootstrap.settings import Settings


async def main() -> None:
    model = build_chat_model(Settings())
    parts: list[str] = []

    async with asyncio.timeout(180):
        async for chunk in model.astream("Explique o que é a boa-fé objetiva"):
            parts.append(chunk.text)
            print(chunk.text, end="", flush=True)

    print("\nCaracteres recebidos:", len("".join(parts)))


if __name__ == "__main__":
    asyncio.run(main())
