from validators import parse_int, validate_non_empty
from books import search_books, get_available_books, get_issued_books
from users import find_user
from library import add_book, remove_book, register_user, issue_book, return_book

books = [
    {
        "id": 1,
        "title": "Inglorious Empire",
        "author": "Sashi Tharoor",
        "available": True,
        "issued_to": None
    }
]

users = [
    {
        "id": 1,
        "name": "Pritam"
    }
]

def main():
    while True:
        print("\n CLI Library Management System")
        print("1. Add book")
        print("2. Remove book")
        print("3. Search book")
        print("4. Register user")
        print("5. Issue book")
        print("6. Return book")
        print("7. List available books")
        print("8. List issued books")
        print("9. Exit")

        choice = input("Enter choice (1-9): ").strip()

        if choice == "9":
            print("Goodbye!")
            break

        try:
            if choice == "1":
                b_id = parse_int(input("Enter Book ID: "), "Book ID")
                title = validate_non_empty(input("Enter Title: "), "Title")
                author = validate_non_empty(input("Enter Author: "), "Author")
                add_book(books, b_id, title, author)
                print("Book added successfully.")

            elif choice == "2":
                b_id = parse_int(input("Enter Book ID to remove: "), "Book ID")
                remove_book(books, b_id)
                print("Book removed successfully.")

            elif choice == "3":
                q = validate_non_empty(input("Enter search query: "), "Search query")
                res = search_books(books, q)
                if not res:
                    print("No books found.")
                else:
                    for b in res:
                        status = "Available" if b["available"] else f"Issued to User {b['issued_to']}"
                        print(f"ID: {b['id']} | Title: {b['title']} | Author: {b['author']} | Status: {status}")

            elif choice == "4":
                u_id = parse_int(input("Enter User ID: "), "User ID")
                name = validate_non_empty(input("Enter Name: "), "Name")
                register_user(users, u_id, name)
                print("User registered successfully.")

            elif choice == "5":
                b_id = parse_int(input("Enter Book ID: "), "Book ID")
                u_id = parse_int(input("Enter User ID: "), "User ID")
                issue_book(books, users, b_id, u_id)
                print("Book issued successfully.")

            elif choice == "6":
                b_id = parse_int(input("Enter Book ID: "), "Book ID")
                return_book(books, b_id)
                print("Book returned successfully.")

            elif choice == "7":
                avail = get_available_books(books)
                if not avail:
                    print("No available books.")
                else:
                    for b in avail:
                        print(f"ID: {b['id']} | Title: {b['title']} | Author: {b['author']}")

            elif choice == "8":
                issued = get_issued_books(books)
                if not issued:
                    print("No issued books.")
                else:
                    for b in issued:
                        u = find_user(users, b["issued_to"])
                        u_name = u["name"] if u else b["issued_to"]
                        print(f"ID: {b['id']} | Title: {b['title']} | Issued to: {u_name}")

            else:
                print("Invalid choice, try again.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
