from contextlib import asynccontextmanager
from fastapi import FastAPI, Query

from app.schemas import QueryResponse
from app.core import lifespan
from app.core import extraction


app = FastAPI(title="Python RAG Project", lifespan=lifespan)


@app.get("/")
def read_root():
    return {"title": "Python RAG Project"}


@app.get("/search")
def read_item(query: str = Query(..., description="Query usada na busca")):
    return QueryResponse(query=query, results=[])

@app.get("/normalize")
def normalize_doc():
    extraction.extract_doc()
    return {"message": "Documento normalizado"}