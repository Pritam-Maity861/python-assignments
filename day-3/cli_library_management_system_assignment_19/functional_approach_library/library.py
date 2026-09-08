from books import create_book, find_book
from users import create_user, find_user
from validators import check_unique_book_id, check_unique_user_id
from exceptions import (
    BookNotFoundError, UserNotFoundError, 
    BookUnavailableError, BookNotIssuedError, LibraryError
)

def add_book(books, book_id, title, author):
    check_unique_book_id(books, book_id)
    book = create_book(book_id, title, author)
    books.append(book)
    return book

def remove_book(books, book_id):
    book = find_book(books, book_id)
    if not book:
        raise BookNotFoundError(f"Book ID {book_id} not found.")
    if not book["available"]:
        raise LibraryError(f"Cannot remove book ID {book_id} because it is issued.")
    books.remove(book)
    return book

def register_user(users, user_id, name):
    check_unique_user_id(users, user_id)
    user = create_user(user_id, name)
    users.append(user)
    return user

def issue_book(books, users, book_id, user_id):
    user = find_user(users, user_id)
    if not user:
        raise UserNotFoundError(f"User ID {user_id} does not exist.")
    book = find_book(books, book_id)
    if not book:
        raise BookNotFoundError(f"Book ID {book_id} not found.")
    if not book["available"]:
        raise BookUnavailableError(f"Book '{book['title']}' is already issued.")
    book["available"] = False
    book["issued_to"] = user_id
    return book

def return_book(books, book_id):
    book = find_book(books, book_id)
    if not book:
        raise BookNotFoundError(f"Book ID {book_id} not found.")
    if book["available"]:
        raise BookNotIssuedError(f"Book '{book['title']}' is not issued.")
    book["available"] = True
    book["issued_to"] = None
    return book
