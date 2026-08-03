from pydantic import BaseModel
from typing import Dict, Any

class SearchResult(BaseModel):
    node_id: str
    score: float
    text: str
    metadata: Dict[str, Any]
