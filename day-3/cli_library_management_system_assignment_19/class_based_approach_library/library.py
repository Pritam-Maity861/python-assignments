from books import Book
from users import User
from exceptions import (
    LibraryException, BookNotFoundError, UserNotFoundError,
    BookUnavailableError, BookNotIssuedError, DuplicateIDError
)

class Library:
    def __init__(self):
        self.books = [
            Book(1, "Inglorious Empire", "Sashi Tharoor")
        ]
        self.users = [
            User(1, "Pritam")
        ]

    def add_book(self, book_id, title, author):
        for b in self.books:
            if b.id == book_id:
                raise DuplicateIDError(f"Book ID {book_id} already exists.")
        book = Book(book_id, title, author)
        self.books.append(book)

    def remove_book(self, book_id):
        book = self.find_book(book_id)
        if not book.available:
            raise LibraryException(f"Cannot remove book ID {book_id} because it is issued.")
        self.books.remove(book)

    def register_user(self, user_id, name):
        for u in self.users:
            if u.id == user_id:
                raise DuplicateIDError(f"User ID {user_id} already exists.")
        user = User(user_id, name)
        self.users.append(user)

    def find_book(self, book_id):
        for b in self.books:
            if b.id == book_id:
                return b
        raise BookNotFoundError(f"Book ID {book_id} not found.")

    def find_user(self, user_id):
        for u in self.users:
            if u.id == user_id:
                return u
        raise UserNotFoundError(f"User ID {user_id} does not exist.")

    def issue_book(self, book_id, user_id):
        user = self.find_user(user_id)
        book = self.find_book(book_id)
        if not book.available:
            raise BookUnavailableError(f"Book '{book.title}' is already issued.")
        book.available = False
        book.issued_to = user.id

    def return_book(self, book_id):
        book = self.find_book(book_id)
        if book.available:
            raise BookNotIssuedError(f"Book '{book.title}' is not issued.")
        book.available = True
        book.issued_to = None

    def search_books(self, query):
        q = query.lower().strip()
        res = []
        for b in self.books:
            if q in b.title.lower() or q in b.author.lower() or q == str(b.id):
                res.append(b)
        return res

    def get_available_books(self):
        return [b for b in self.books if b.available]

    def get_issued_books(self):
        return [b for b in self.books if not b.available]
