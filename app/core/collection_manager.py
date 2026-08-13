from qdrant_client import QdrantClient
from qdrant_client.http import models
from sentence_transformers import SentenceTransformer



class CollectionManager:
    model_name = "BAAI/bge-small-en-v1.5"
    collection_name = "books_0.21"
    vector_size = 384 # ia ser 1024, mas para o modelo atual será 384
    distance = models.Distance.COSINE

    @staticmethod
    def ensure_setup(client: QdrantClient):
        model_name = CollectionManager.model_name
        collection_name = CollectionManager.collection_name
        vector_size = CollectionManager.vector_size
        distance = CollectionManager.distance

        
        assert SentenceTransformer(model_name).get_sentence_embedding_dimension() == CollectionManager.vector_size, "O vector_size precisa estar alinhado com com a dimensão do modelo!"

        # seta o modelo
        client.set_model(CollectionManager.model_name)
        
        if not client.collection_exists(collection_name=collection_name):
            print(f"Coleção '{collection_name}' não existe. Criando...")

            # pega a instância padrão
            fastembed_vectors_config = client.get_fastembed_vector_params(on_disk=None)

            client.create_collection(
                collection_name=collection_name,
                vectors_config=fastembed_vectors_config
            )

            CollectionManager.insert_mock_data(client)
        else:
            print(f"Coleção '{collection_name}' já existe.")

        print(f"Coleção '{collection_name}' configurada e pronta pra uso.")

    @staticmethod
    def insert_mock_data(client: QdrantClient):
        ids = [1, 2]
        documents = [
            "How to configure SSO in enterprise settings.",
            "Troubleshooting slow database queries in PostgreSQL.",
        ]
        metadata = [
            {"author": "Alice", "category": "Auth", "doc_id": "DOC-101"},
            {"author": "Bob", "category": "Database", "doc_id": "DOC-102"},
        ]

        client.add(
            collection_name=CollectionManager.collection_name,
            documents=documents,
            metadata=metadata,
            ids=ids,
        )
