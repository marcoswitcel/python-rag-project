from contextlib import asynccontextmanager
from fastapi import FastAPI

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


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str):
    return {"item_id": item_id, "q": q}
