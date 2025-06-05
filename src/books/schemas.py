from typing import Optional
from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    author: str
    category: str
    published_date: str

class BookUpdateModel(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None


