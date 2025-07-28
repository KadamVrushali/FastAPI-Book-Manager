import json
from pathlib import Path
from .models import Book
from typing import List

# Get dynamic path to books.json
DATA_FILE = Path(__file__).resolve().parent / "books.json"

def load_books() -> List[Book]:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        books_raw = json.load(f)
        return [Book(**book) for book in books_raw]

def save_books(books: List[Book]):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([book.dict() for book in books], f, indent=2)
