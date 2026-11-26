import asyncio

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from rag_juridico.bootstrap.models import build_chat_model
from rag_juridico.bootstrap.settings import Settings


async def main() -> None:
    prompt = ChatPromptTemplate.from_template("Explique {term} em uma frase.")
    chain = prompt | build_chat_model(Settings()) | StrOutputParser()
    terms = ("mora", "prescrição", "minuta", "decadência")
    inputs = [{"term": term} for term in terms]
    results = await chain.abatch(
        inputs,
        config={"max_concurrency": 2, "tags": ["legal-study"]},
    )
    for item, result in zip(inputs, results, strict=True):
        print(f"{item['term']}: {result}")


if __name__ == "__main__":
    asyncio.run(main())
