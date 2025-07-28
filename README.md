---

# 📚 FastAPI Book Manager

A FastAPI-based application to manage a collection of books with full **CRUD functionality**, real-time updates via **WebSockets**, **pagination**, **sorting**, and **filtering** — all using a simple **JSON file** for storage.

---

## 🚀 Features

* ✅ **Create/Update Book**

  * Combines create & update into a single endpoint
  * Updates if:

    * ISBN already exists, OR
    * Same `title`, `author`, and `publication_year`
  * Creates a new entry otherwise
  * Validates ISBN uniqueness
  * Validates `publication_year` between 1450 and current year

* ✅ **Retrieve All Books**

  * Supports **pagination** (`skip`, `limit`)
  * Supports **sorting** by `title`, `author`, or `publication_year` (asc/desc)
  * Supports **filtering** by `genre` or `author`

* ✅ **Delete Book by ID**

* ✅ **Real-Time Updates** via WebSocket

  * Clients receive updates on book additions, deletions, and modifications instantly

* ✅ **Thread-Safe File Access** using Lock

* ✅ **Data Stored in `books.json`** (No Database Used)

---

## 📁 Project Structure

```
app/
│
├── main.py               # FastAPI app and routes
├── models.py             # Pydantic models and validation
├── utils.py              # Utility functions for file I/O
├── websocket_manager.py  # Manages WebSocket connections
├── books.json            # Book data (used for storage)
```

---

## 🛠️ Setup & Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/your-username/fastapi-book-manager.git
cd fastapi-book-manager
```

### 2. Install dependencies

```bash
pip install fastapi uvicorn
```

### 3. Run the server

```bash
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000/docs` for the interactive API documentation (Swagger UI).

---

## 📡 WebSocket Testing

To test real-time updates:

1. Open a WebSocket client (e.g., [Hoppscotch](https://hoppscotch.io/websocket) or browser extension).
2. Connect to:
   `ws://127.0.0.1:8000/ws/books`
3. Perform any create/update/delete operations.
4. You will receive updated book data instantly!

---

## 🧪 Example API Requests

### Create or Update a Book

```http
POST /books
Content-Type: application/json

{
  "title": "Atomic Habits",
  "author": "James Clear",
  "publication_year": 2018,
  "genre": "Self-help",
  "isbn": "1234567890"
}
```

### Get All Books with Pagination, Filtering, Sorting

```http
GET /books?skip=0&limit=10&genre=Fiction&sort_by=title&sort_order=asc
```

### Delete a Book

```http
DELETE /books/1
```

---

## 📄 Assignment Requirements Met

| Feature                                | Status ✅ |
| -------------------------------------- | -------- |
| JSON-based storage only                | ✅        |
| Combined create/update with validation | ✅        |
| ISBN uniqueness + year validation      | ✅        |
| Pagination, filtering, sorting         | ✅        |
| WebSocket for real-time updates        | ✅        |
| Thread-safe file handling              | ✅        |
| Meaningful error handling              | ✅        |

---

## ✨ Credits

Developed by **Vrushali Kadam**
Built with ❤️ using FastAPI

---

