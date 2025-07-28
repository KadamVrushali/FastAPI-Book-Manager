from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Query, HTTPException
from typing import List, Optional
from .models import Book
from . import db
from .websocket_manager import manager

app = FastAPI()

@app.get("/books", response_model=List[Book])
def get_books(
    skip: int = 0,
    limit: int = 10,
    author: Optional[str] = None,
    genre: Optional[str] = None,
    sort_by: Optional[str] = Query(None, regex="^(title|author|publication_year)$"),
    sort_order: Optional[str] = Query("asc", regex="^(asc|desc)$")
):
    books = db.load_books()

    # Filtering
    if author:
        books = [book for book in books if book.author.lower() == author.lower()]
    if genre:
        books = [book for book in books if book.genre.lower() == genre.lower()]

    # Sorting
    if sort_by:
        reverse = sort_order == "desc"
        books.sort(key=lambda x: getattr(x, sort_by), reverse=reverse)

    return books[skip: skip + limit]

@app.post("/books", response_model=Book)
async def add_book(book: Book):
    books = db.load_books()
    book.id = (max([b.id for b in books]) + 1) if books else 1
    books.append(book)
    db.save_books(books)
    await manager.broadcast({"event": "new_book", "book": book.dict()})
    return book

@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, updated_book: Book):
    books = db.load_books()
    for i, book in enumerate(books):
        if book.id == book_id:
            updated_book.id = book_id
            books[i] = updated_book
            db.save_books(books)
            await manager.broadcast({"event": "update_book", "book": updated_book.dict()})
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    books = db.load_books()
    books = [book for book in books if book.id != book_id]
    db.save_books(books)
    await manager.broadcast({"event": "delete_book", "book_id": book_id})
    return {"message": f"Book {book_id} deleted"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()  # Keeps connection alive
    except WebSocketDisconnect:
        manager.disconnect(websocket)
