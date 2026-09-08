def create_book(book_id, title, author):
    return {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True,
        "issued_to": None
    }

def find_book(books, book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None

def search_books(books, query):
    q = query.lower().strip()
    res = []
    for b in books:
        if q in b["title"].lower() or q in b["author"].lower() or q == str(b["id"]):
            res.append(b)
    return res

def get_available_books(books):
    return [b for b in books if b["available"]]

def get_issued_books(books):
    return [b for b in books if not b["available"]]
