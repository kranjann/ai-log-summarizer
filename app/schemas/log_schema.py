from pydantic import BaseModel
from typing import List


class LogAnalysis(BaseModel):
    summary: str
    root_cause: str
    severity: str
    recommendations: List[str]