from qdrant_client import QdrantClient
from qdrant_client.http import models
from sentence_transformers import SentenceTransformer
from llama_index.core import Document, VectorStoreIndex, StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore



class CollectionManager:
    model_name = "BAAI/bge-small-en-v1.5"
    collection_name = "books_0.38"
    vector_size = 384 # ia ser 1024, mas para o modelo atual será 384
    distance = models.Distance.COSINE

    @staticmethod
    def ensure_setup(client: QdrantClient):
        model_name = CollectionManager.model_name
        collection_name = CollectionManager.collection_name
        vector_size = CollectionManager.vector_size
        distance = CollectionManager.distance

        
        assert SentenceTransformer(model_name).get_sentence_embedding_dimension() == CollectionManager.vector_size, "O vector_size precisa estar alinhado com com a dimensão do modelo!"

        if not client.collection_exists(collection_name=collection_name):
            print(f"Coleção '{collection_name}' não existe. Criando...")

            client.create_collection(
                collection_name=collection_name,
                vectors_config=models.VectorParams(
                    size=vector_size,
                    distance=distance
                )
            )

            CollectionManager.insert_mock_data(client)
        else:
            print(f"Coleção '{collection_name}' já existe.")

        print(f"Coleção '{collection_name}' configurada e pronta pra uso.")

    @staticmethod
    def insert_mock_data(client: QdrantClient):
        print("Inserindo dados mockados...")

        documents = [
            Document(
                text="How to configure SSO in enterprise settings.",
                metadata={"author": "Alice", "category": "Auth", "doc_id": "DOC-101"}
            ),
            Document(
                text="Troubleshooting slow database queries in PostgreSQL.",
                metadata={"author": "Bob", "category": "Database", "doc_id": "DOC-102"}
            ),
        ]

        vector_store = QdrantVectorStore(
            collection_name=CollectionManager.collection_name,
            client=client,
        )

        # configuração de persistência
        storage_context = StorageContext.from_defaults(vector_store=vector_store)

        # delega a persistência para o llamaIndex
        VectorStoreIndex.from_documents(
            documents,
            storage_context=storage_context
        )
