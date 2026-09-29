import os
import chromadb
import uuid

# Initialize ChromaDB client (local persistent storage)
DB_PATH = os.path.expanduser("~/.hindsight/db")
os.makedirs(DB_PATH, exist_ok=True)

chroma_client = chromadb.PersistentClient(path=DB_PATH)
collection = chroma_client.get_or_create_collection(name="hindsight_memory")

def add_to_memory(query: str, response: str, metadata: dict = None):
    """
    Add a query and response pair to the vector database.
    """
    if metadata is None:
        metadata = {"source": "user_interaction"}
        
    doc_id = str(uuid.uuid4())
    content = f"Query: {query}\nResponse: {response}"
    
    collection.add(
        documents=[content],
        metadatas=[metadata],
        ids=[doc_id]
    )

def retrieve_context(query: str, n_results: int = 3) -> str:
    """
    Retrieve relevant past interactions based on the current query.
    """
    if collection.count() == 0:
        return ""
        
    results = collection.query(
        query_texts=[query],
        n_results=min(n_results, collection.count())
    )
    
    if not results['documents']:
        return ""
        
    contexts = results['documents'][0]
    return "\n\n---\n\n".join(contexts)
