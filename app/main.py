from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI, Query

from app.schemas import QueryResponse
from app.core import lifespan, doc_converter

app = FastAPI(title="Python RAG Project", lifespan=lifespan)


@app.get("/")
def read_root():
    return {"title": "Python RAG Project"}


@app.get("/search")
def read_item(query: str = Query(..., description="Query usada na busca")):
    return QueryResponse(query=query, results=[])

"""
    Método criado temporariamente para testar a conversão do documento para markdown
    Por enquanto está definido de forma estática o endereço e arquivo a ser convertido    
"""
@app.get("/doc_converter")
def document_converter():
    input_file = Path("./data/raw/dom-casmurro/pg55752-images.html")
    doc_converter(input_path=input_file, file_name="dom-casmurro.md")
    return {"message": "The document has been converted to markdown."}