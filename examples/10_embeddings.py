from rag_juridico.bootstrap.models import build_embeddings
from rag_juridico.bootstrap.settings import Settings


def main() -> None:
    embeddings = build_embeddings(Settings())
    vector = embeddings.embed_query("Responsabilidade civil por dano moral")
    documents = embeddings.embed_documents(
        [
            "Reparação de danos extrapatrimoniais.",
            "Prazo de rescisão contratual.",
        ]
    )
    print("Dimensão:", len(vector))
    print("Primeiros valores:", vector[:5])
    print("Documentos:", len(documents))


if __name__ == "__main__":
    main()
