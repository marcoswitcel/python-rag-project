from contextlib import asynccontextmanager
from fastapi import FastAPI
from llama_index.core import Settings
from qdrant_client import QdrantClient
from llama_index.vector_stores.qdrant import QdrantVectorStore
import os


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application Startup")
    print("Recuperando recursos globais...")

    # Desabilitando LLM
    Settings.llm = None

    qdrant_url = os.getenv("QDRANT_URL", "http://localhost:6333")

    try:
        client = QdrantClient(url=qdrant_url)
        # força a fazer uma conexão e faz falhar no startup se o serviço estiver fora
        client.get_collections()
        print("Conectado ao Qdrant")
    except Exception as e:
        raise RuntimeError(f"Não foi possível conectar ao servidor Qdrant no endereço: '{qdrant_url}': causa {e}")

    yield

    print("Application Shutdown")
    print("Liberando recursos...")
