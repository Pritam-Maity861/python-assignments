from exceptions import DuplicateIDError

def parse_int(val_str, name="ID"):
    val = val_str.strip()
    if not val.isdigit():
        raise ValueError(f"{name} must be a positive number.")
    return int(val)

def validate_non_empty(val_str, name="Field"):
    cleaned = val_str.strip()
    if not cleaned:
        raise ValueError(f"{name} cannot be empty.")
    return cleaned

def check_unique_book_id(books, book_id):
    for b in books:
        if b["id"] == book_id:
            raise DuplicateIDError(f"Book ID {book_id} already exists.")

def check_unique_user_id(users, user_id):
    for u in users:
        if u["id"] == user_id:
            raise DuplicateIDError(f"User ID {user_id} already exists.")
