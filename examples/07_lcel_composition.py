from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
)


def normalize(question: str) -> str:
    return " ".join(question.strip().split())


def main() -> None:
    normalize_question = RunnableLambda(normalize)
    pipeline = RunnableParallel(
        original=RunnablePassthrough(),
        normalized=normalize_question,
    ) | RunnablePassthrough.assign(
        length=RunnableLambda(lambda data: len(data["normalized"]))
    )

    print(pipeline.invoke("    O que é      mora?         "))


if __name__ == "__main__":
    main()
