from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from dotenv import load_dotenv
import os

from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI

class Item(BaseModel):
    question: str

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    print("API key loaded successfully.")
else:
    print("Failed to load API key.")
    
storage_context = StorageContext.from_defaults(persist_dir="ml_index")
index = load_index_from_storage(storage_context)

engine = index.as_query_engine()

app = FastAPI()
@app.post("/")
async def query(item: Item):
    response = engine.query(item.question)
    return {"response": str(response)}

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)