import os

from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    print("API Key loaded successfully.")
    print(f"API Key: {api_key[0:8]}")
else:
    print("Failed to load API Key.")

# Load documents from the 'pdf' directory
documents = SimpleDirectoryReader('pdf').load_data()

index = VectorStoreIndex.from_documents(documents)
engine = index.as_query_engine()
result = engine.query("What are the strengths of R over Python?")
print(result)

index.storage_context.persist("ml_index")
