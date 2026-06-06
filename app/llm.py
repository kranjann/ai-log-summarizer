from openai import OpenAI
from dotenv import load_dotenv
from prompts import LOG_ANALYZER_PROMPT
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
                "content": LOG_ANALYZER_PROMPT
            },
            {
                "role": "user",
                "content": log_text
            }
        ]
    )

    return response.choices[0].message.content