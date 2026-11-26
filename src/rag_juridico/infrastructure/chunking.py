from uuid import NAMESPACE_URL, uuid5

from langchain_text_splitters import RecursiveCharacterTextSplitter

from rag_juridico.domain.evidence import Evidence
from rag_juridico.domain.legal_document import LegalDocument


class RecursiveChunker:
    def __init__(self, chunk_size: int, chunk_overlap: int) -> None:
        self._splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", " ", "", ". "],
        )

    def split(self, documents: list[LegalDocument]) -> list[Evidence]:
        result: list[Evidence] = []
        for document in documents:
            for index, chunk in enumerate(self._splitter.split_text(document.content)):
                if chunk.strip():
                    identifier = uuid5(
                        NAMESPACE_URL,
                        f"{document.source}-{document.page}:{index}:{chunk}",
                    )
                    result.append(
                        Evidence(
                            id=str(identifier),
                            source=document.source,
                            content=chunk,
                            page=document.page,
                        )
                    )
        return result
