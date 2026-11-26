import argparse
from pathlib import Path

from rag_juridico.bootstrap.container import build_ingestion, build_search
from rag_juridico.bootstrap.settings import Settings


def main() -> None:
    parser = argparse.ArgumentParser(description="RAG Jurídico CLI")
    parser.add_argument("command", choices=["ingest", "search"])
    parser.add_argument("value")
    args = parser.parse_args()
    settings = Settings()

    if args.command == "ingest":
        print("Indexed chunks:", build_ingestion(settings).execute(Path(args.value)))
    elif args.command == "search":
        for item in build_search(settings).execute(args.value):
            print(f"\n{item.source} / page {item.page} / {item.id}\n{item.content}")


if __name__ == "__main__":
    main()
