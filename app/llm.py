from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def analyze_logs(log_text: str):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": """
                You are a senior SRE engineer.

                Analyze logs and provide:
                1. Summary
                2. Root Cause
                3. Severity
                4. Recommendation
                """
            },
            {
                "role": "user",
                "content": log_text
            }
        ]
    )

    return response.choices[0].message.content