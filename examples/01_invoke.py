from langchain_core.messages import HumanMessage, SystemMessage

from rag_juridico.bootstrap.models import build_chat_model
from rag_juridico.bootstrap.settings import Settings


def main() -> None:
    model = build_chat_model(Settings())
    messages = [
        SystemMessage(content="Explique conceitos jurídicos em português."),
        HumanMessage(content="O que é o direito de autodeterminação dos povos?"),
    ]
    response = model.invoke(messages)
    print(response.text)


if __name__ == "__main__":
    main()
