import os
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print(api_key[0:6])

documents = SimpleDirectoryReader("pdf").load_data()

index = VectorStoreIndex.from_documents(documents)

index.storage_context.persist("faq_index")
