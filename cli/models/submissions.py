from pydantic import BaseModel

class Submission(BaseModel):
    id: int
    status: str
    title: str
    runtime: str
    memory: str
