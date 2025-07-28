from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

CURRENT_YEAR = datetime.now().year

class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    publication_year: int = Field(..., ge=1450, le=CURRENT_YEAR)
    genre: str
    isbn: str
