from pydantic import BaseModel
from typing import List, Optional

class Problem(BaseModel):
    id: int
    title: str
    difficulty: str
    paid_only: bool
    tags: Optional[List[str]] = []
