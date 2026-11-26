from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
)

from rag_juridico.bootstrap.models import build_chat_model
from rag_juridico.bootstrap.settings import Settings


def retrieve_demo(question: str) -> str:
    if "rescis" in question.casefold() or "rescind" in question.casefold():
        return "[E1] Contrato fictício, cláusula 3: aviso prévio de 30 dias."
    return "Nenhuma evidência encontrada."


def main() -> None:
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Responda só com o contexto. Cite o ID. Se faltar evidência, informe.",
            ),
            ("human", "Contexto: {context}\nPergunta: {question}"),
        ]
    )
    chain = (
        RunnableParallel(
            context=RunnableLambda(retrieve_demo),
            question=RunnablePassthrough(),
        )
        | prompt
        | build_chat_model(Settings())
        | StrOutputParser()
    )

    question = "Qual é o praso de rescisão?"
    print(chain.invoke(question))
    print("\nStreaming:")
    for text in chain.stream(question):
        print(text, end="", flush=True)
    print()


if __name__ == "__main__":
    main()
