from pydantic import BaseModel
from typing import List

from .search_result import SearchResult

class Query(BaseModel):
    query: str

class QueryResponse(BaseModel):
    query: str
    results: List[SearchResult]
