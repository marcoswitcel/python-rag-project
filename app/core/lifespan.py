from contextlib import asynccontextmanager
from fastapi import FastAPI
from llama_index.core import Settings, VectorStoreIndex
from qdrant_client import QdrantClient
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from app.core.collection_manager import CollectionManager
import os


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application Startup")
    print("Recuperando recursos globais...")

    # Desabilitando LLM
    Settings.llm = None

    # Setando embeder
    Settings.embed_model = HuggingFaceEmbedding(
        model_name="BAAI/bge-small-en-v1.5",
        device="cuda" if os.getenv("USE_CUDA") == "1" else "cpu",
        normalize=True,
    )

    qdrant_url = os.getenv("QDRANT_URL", "http://localhost:6333")

    try:
        client = QdrantClient(url=qdrant_url)
        # Mover esse check para um endpoint de healthcheck
        # força a fazer uma conexão e faz falhar no startup se o serviço estiver fora
        client.get_collections()
        print("Conectado ao Qdrant")
    except Exception as e:
        raise RuntimeError(f"Não foi possível conectar ao servidor Qdrant no endereço: '{qdrant_url}': causa {e}")

    CollectionManager.ensure_setup(client)

    vector_store = QdrantVectorStore(
        collection_name=CollectionManager.collection_name,
        client=client,
    )

    index = VectorStoreIndex.from_vector_store(vector_store=vector_store)

    # Instancia um recuperador de registros
    retriever = index.as_retriever(similarity_top_k=10)

    # Export
    app.state.qdrant_client = client
    app.state.vector_store = vector_store
    app.state.retriever = retriever

    yield

    print("Application Shutdown")
    print("Liberando recursos...")
