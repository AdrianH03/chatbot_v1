from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from dotenv import load_dotenv
import os
import openai
from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI

class Query(BaseModel):
    question: "str"

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print(api_key[0:6])

context = StorageContext.from_defaults(persist_dir = "faq_index")
index = load_index_from_storage(context)

engine = index.as_query_engine()
app = FastAPI()

@app.post("/")
async def query(query: Query):
    result = engine.query(query.question)
    return(result)

if __name__ == "__main__":
    uvicorn.run("cum_server:app", host = "127.0.0.1", port = 8000, reload = True)