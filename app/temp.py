from services.embedding_service import generate_embedding
import os

print("Current Working Directory:", os.getcwd())

text = "PostgreSQL connection pool exhausted"

embedding = generate_embedding(text)

print(type(embedding))
print(len(embedding))
print(embedding[:5])