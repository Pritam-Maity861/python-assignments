class Book:
    def __init__(self, book_id, title, author, available=True, issued_to=None):
        self.id = book_id
        self.title = title
        self.author = author
        self.available = available
        self.issued_to = issued_to
