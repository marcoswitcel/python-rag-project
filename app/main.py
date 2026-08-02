from contextlib import asynccontextmanager
from fastapi import FastAPI, Query

from app.schemas import QueryResponse

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application Startup")
    print("Recuperando recursos globais...")

    yield

    print("Application Shutdown")
    print("Liberando recursos...")



app = FastAPI(title="Python RAG Project", lifespan=lifespan)


@app.get("/")
def read_root():
    return {"title": "Python RAG Project"}


@app.get("/search")
def read_item(query: str = Query(..., description="Query usada na busca")):
    return QueryResponse(query=query, results=[])
