import json

from openai import OpenAI
from app.config import OPENAI_API_KEY
from app.prompts import LOG_ANALYZER_PROMPT
from app.schemas.log_schema import LogAnalysis


class LLMService:

    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def analyze_logs(self, log_text: str) -> LogAnalysis:

        response = self.client.chat.completions.create(
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

        result = response.choices[0].message.content

        data = json.loads(result)

        analysis = LogAnalysis(**data)

        return analysis