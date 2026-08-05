from qdrant_client import QdrantClient
from qdrant_client.http import models


class CollectionManager:
    collection_name = "books"
    vector_size = 1024
    distance = models.Distance.COSINE

    @staticmethod
    def ensure_setup(client: QdrantClient):
        collection_name = CollectionManager.collection_name
        vector_size = CollectionManager.vector_size
        distance = CollectionManager.distance

        if not client.collection_exists(collection_name=collection_name):
            print(f"Coleção '{collection_name}' não existe. Criando...")
            client.create_collection(
                collection_name=collection_name,
                vectors_config=models.VectorParams(
                    size=vector_size,
                    distance=distance
                )
            )
        else:
            print(f"Coleção '{collection_name}' já existe.")

        print(f"Coleção '{collection_name}' configurada e pronta pra uso.")
