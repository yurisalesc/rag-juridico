from langchain_core.messages import AIMessageChunk

from rag_juridico.bootstrap.models import build_chat_model
from rag_juridico.bootstrap.settings import Settings


def main() -> None:
    model = build_chat_model(Settings())
    full: AIMessageChunk | None = None

    for chunk in model.stream("Explique o que é a boa-fé objetiva"):
        print(chunk.text, end="", flush=True)
        full = chunk if full is None else full + chunk

    print()
    if full is not None:
        print("\nCaracteres recebidos:", len(full.text))


if __name__ == "__main__":
    main()
