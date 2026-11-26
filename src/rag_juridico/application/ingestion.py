from pathlib import Path

from rag_juridico.application.ports import Chunker, DocumentLoader, EvidenceWriter


class IngestDocuments:
    def __init__(
        self,
        loader: DocumentLoader,
        chunker: Chunker,
        writer: EvidenceWriter,
    ) -> None:
        self._loader = loader
        self._chunker = chunker
        self._writer = writer

    def execute(self, path: Path) -> int:
        if not path.is_file():
            raise FileNotFoundError(f"File not found: {path}")
        evidence = self._chunker.split(self._loader.load(path))
        self._writer.upsert(evidence)
        return len(evidence)
