from validators import parse_int, validate_non_empty
from library import Library

def main():
    lib = Library()
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
            print("Program Exited!")
            break

        try:
            if choice == "1":
                b_id = parse_int(input("Enter Book ID: "), "Book ID")
                title = validate_non_empty(input("Enter Title: "), "Title")
                author = validate_non_empty(input("Enter Author: "), "Author")
                lib.add_book(b_id, title, author)
                print("Book added successfully.")

            elif choice == "2":
                b_id = parse_int(input("Enter Book ID to remove: "), "Book ID")
                lib.remove_book(b_id)
                print("Book removed successfully.")

            elif choice == "3":
                q = validate_non_empty(input("Enter search query: "), "Search query")
                res = lib.search_books(q)
                if not res:
                    print("No books found.")
                else:
                    for b in res:
                        status = "Available" if b.available else f"Issued to User {b.issued_to}"
                        print(f"ID: {b.id} | Title: {b.title} | Author: {b.author} | Status: {status}")

            elif choice == "4":
                u_id = parse_int(input("Enter User ID: "), "User ID")
                name = validate_non_empty(input("Enter Name: "), "Name")
                lib.register_user(u_id, name)
                print("User registered successfully.")

            elif choice == "5":
                b_id = parse_int(input("Enter Book ID: "), "Book ID")
                u_id = parse_int(input("Enter User ID: "), "User ID")
                lib.issue_book(b_id, u_id)
                print("Book issued successfully.")

            elif choice == "6":
                b_id = parse_int(input("Enter Book ID: "), "Book ID")
                lib.return_book(b_id)
                print("Book returned successfully.")

            elif choice == "7":
                avail = lib.get_available_books()
                if not avail:
                    print("No available books.")
                else:
                    for b in avail:
                        print(f"ID: {b.id} | Title: {b.title} | Author: {b.author}")

            elif choice == "8":
                issued = lib.get_issued_books()
                if not issued:
                    print("No issued books.")
                else:
                    for b in issued:
                        try:
                            u = lib.find_user(b.issued_to)
                            u_name = u.name
                        except Exception:
                            u_name = b.issued_to
                        print(f"ID: {b.id} | Title: {b.title} | Issued to: {u_name}")

            else:
                print("Invalid choice, try again.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
