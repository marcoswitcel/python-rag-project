from contextlib import asynccontextmanager
from fastapi import FastAPI
from llama_index.core import Settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application Startup")
    print("Recuperando recursos globais...")

    # Desabilitando LLM
    Settings.llm = None

    yield

    print("Application Shutdown")
    print("Liberando recursos...")
