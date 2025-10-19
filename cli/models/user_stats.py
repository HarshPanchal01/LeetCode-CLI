from pydantic import BaseModel

class UserStats(BaseModel):
    total_problems: int
    solved_problems: int
    acceptance_rate: float
