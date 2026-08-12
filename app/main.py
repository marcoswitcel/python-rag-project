from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI, Query, Depends
from llama_index.core.retrievers import VectorIndexRetriever

from app.schemas import QueryResponse
from app.core import lifespan, doc_converter
from app.core.dependencies import get_retriever
from app.schemas import SearchResult

app = FastAPI(title="Python RAG Project", lifespan=lifespan)


@app.get("/")
def read_root():
    return {"title": "Python RAG Project"}


@app.get("/search")
def read_item(query: str = Query(..., description="Query usada na busca"), retriever: VectorIndexRetriever = Depends(get_retriever)):
    # Faz a query
    nodes = retriever.retrieve(query)

    results = [
        SearchResult(
            node_id=node.node.node_id,
            score=node.score,
            text=node.node.get_content(),
            metadata=node.node.metadata,
        )
        for node in nodes
    ]

    return QueryResponse(query=query, results=results)

"""
    Método criado temporariamente para testar a conversão do documento para markdown
    Por enquanto está definido de forma estática o endereço e arquivo a ser convertido    
"""
@app.get("/doc_converter")
def document_converter():
    input_file = Path("./data/raw/dom-casmurro/pg55752-images.html")
    doc_converter(input_path=input_file, file_name="dom-casmurro.md")
    return {"message": "The document has been converted to markdown."}