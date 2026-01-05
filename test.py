from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    print("API Key loaded successfully.")
    print(f"API Key: {api_key[0:8]}")
else:
    print("Failed to load API Key.")
    
#First API request test
from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5-nano",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)