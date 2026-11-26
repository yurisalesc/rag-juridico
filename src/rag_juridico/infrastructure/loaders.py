from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

from rag_juridico.domain.legal_document import LegalDocument


class LocalDocumentLoader:
    def load(self, path: Path) -> list[LegalDocument]:
        if path.suffix.lower() == ".pdf":
            return [
                LegalDocument(
                    path.name, doc.page_content, int(doc.metadata["page"]) + 1
                )
                for doc in PyPDFLoader(str(path)).load()
                if doc.page_content.strip()
            ]
        if path.suffix.lower() == ".txt":
            content = path.read_text(encoding="utf-8")
            return [LegalDocument(path.name, content)] if content.strip() else []
        raise ValueError(f"Unsupported file format: {path.suffix}")
