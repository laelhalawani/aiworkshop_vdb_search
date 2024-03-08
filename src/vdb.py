import chromadb
#https://docs.trychroma.com/api-reference
# collection.add(
#     documents=["lorem ipsum...", "doc2", "doc3", ...],
#     metadatas=[{"chapter": "3", "verse": "16"}, {"chapter": "3", "verse": "5"}, {"chapter": "29", "verse": "11"}, ...],
#     ids=["id1", "id2", "id3", ...]
# )
vdb_path="./vector_db"
vector_db = chromadb.PersistentClient(vdb_path)

def get_or_create_collection(name, metadata=None):
    return vector_db.get_or_create_collection(name=name, metadata=metadata)

current_collection = get_or_create_collection(name="documents")

def _generate_next_available_id():
    return str(current_collection.count())

def add_embeddings(embeddings, metadatas=None, uris=None):
    current_collection.add(
        ids=[_generate_next_available_id()],
        embeddings=embeddings,
        metadatas=metadatas,
        uris=uris
    )


def find_most_similar_embeddings(query_embeddings, n_results=1, where=None):
    return current_collection.query(
        query_embeddings=query_embeddings,
        n_results=n_results,
        where=where
    )

def list_collections():
    return vector_db.list_collections()

def create_collection(name, metadata=None):
    return vector_db.create_collection(name=name, metadata=metadata)

def get_collection(name):
    return vector_db.get_collection(name=name)

def get_or_create_collection(name, metadata=None):
    return vector_db.get_or_create_collection(name=name, metadata=metadata)

def peek():
    return current_collection.peek()

