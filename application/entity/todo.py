from pydantic import BaseModel
from datetime import date


class Todo(BaseModel):
    id: int = None
    title: str = None
    description: str = None
    date: date = None
