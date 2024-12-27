from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from pymilvus import Collection, connections, utility
from ollama import Ollama

# Initialize FastAPI
app = FastAPI()

# Connect to Milvus database
MILVUS_HOST = "127.0.0.1"
MILVUS_PORT = "19530"
connections.connect(host=MILVUS_HOST, port=MILVUS_PORT)

# Specify the Milvus collection
COLLECTION_NAME = "document_vectors"
if not utility.has_collection(COLLECTION_NAME):
    raise ValueError(f"Milvus collection '{COLLECTION_NAME}' does not exist.")
collection = Collection(COLLECTION_NAME)

# Initialize Ollama LLM
ollama_client = Ollama()

# Define input schema
class ChatRequest(BaseModel):
    user_query: str
    top_k: int = 5  # Number of top results to retrieve from Milvus

# Define response schema
class ChatResponse(BaseModel):
    response: str
    relevant_documents: List[str]

# Helper function to query Milvus
def query_milvus(query_vector: List[float], top_k: int) -> List[str]:
    search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
    results = collection.search(
        data=[query_vector],
        anns_field="embedding",
        param=search_params,
        limit=top_k,
        output_fields=["text"]
    )
    documents = [hit.entity.get("text") for hit in results[0]]
    return documents

# Helper function to get embedding from Ollama
def get_embedding(text: str) -> List[float]:
    response = ollama_client.embedding(text=text)
    return response["embedding"]

# Endpoint to handle chat requests
@app.post("/chat", response_model=ChatResponse)
def chat_with_llm(request: ChatRequest):
    try:
        # Get query embedding
        query_embedding = get_embedding(request.user_query)

        # Retrieve relevant documents from Milvus
        relevant_docs = query_milvus(query_embedding, request.top_k)

        # Combine user query with relevant documents
        combined_input = request.user_query + "\n\nRelevant information:\n" + "\n".join(relevant_docs)

        # Generate response from Ollama
        llm_response = ollama_client.chat(prompt=combined_input)

        return ChatResponse(response=llm_response, relevant_documents=relevant_docs)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Example endpoint to test server health
@app.get("/health")
def health_check():
    return {"status": "ok"}
