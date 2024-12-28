from pydantic import BaseModel
from typing import Optional
#data models like task schema
class Task(BaseModel):
    title: str
    description: Optional[str]
    deadline: str
    priority: int
