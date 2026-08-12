from fastapi import Request
from qdrant_client import QdrantClient
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core.retrievers import VectorIndexRetriever


def get_qdrant_client(request: Request) -> QdrantClient:
    """Retorna a instância QdrantClient configurada globalmente."""
    return request.app.state.qdrant_client

def get_vector_store(request: Request) -> QdrantVectorStore:
    """Retorna a instância QdrantVectorStore configurada globalmente."""
    return request.app.state.vector_store

def get_retriever(request: Request) -> VectorIndexRetriever:
    """Retorna a instância VectorIndexRetriever configurada globalmente."""
    return request.app.state.retriever