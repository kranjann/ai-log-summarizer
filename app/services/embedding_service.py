from dotenv import load_dotenv
import os

load_dotenv()

# print("OPENAI_API_KEY =", os.getenv("OPENAI_API_KEY"))

from openai import OpenAI

client = OpenAI()

print("Client created successfully")


def generate_embedding(text: str):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding