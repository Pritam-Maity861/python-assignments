'''
4. Contact Manager 
contacts = [ 
    { 
        "name": "Tarun", 
        "phone": "9876543210", 
        "email": "tarun@example.com" 
    } 
] 
Implement: 
add_contact() 
delete_contact() 
search_contact() 
update_contact() 
list_contacts() 
Requirements 
● Phone number cannot be empty 
● Email cannot be empty 
● Duplicate contacts should be rejected 
● Searching for a missing contact should produce a meaningful error 
● Split the program into modules
'''

'''
class base approach
'''

class ContactManager:

    def __init__(self):
        self.contacts = [
            {
                "name": "Tarun",
                "phone": "9876543210",
                "email": "tarun@example.com"
            }
        ]

    def add_contact(self, name, phone, email):

        if phone == "":
            print("Phone number cannot be empty.")
            return

        if email == "":
            print("Email cannot be empty.")
            return

        for contact in self.contacts:
            if contact["name"].lower() == name.lower():
                print("Contact already exists.")
                return

        self.contacts.append({
            "name": name,
            "phone": phone,
            "email": email
        })

        print("Contact added successfully.")

    def delete_contact(self, name):

        for contact in self.contacts:
            if contact["name"].lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return

        print("Contact not found.")

    def search_contact(self, name):

        for contact in self.contacts:
            if contact["name"].lower() == name.lower():
                print("\nContact found:")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                return

        print("Contact not found.")

    def update_contact(self, name, phone, email):

        if phone == "":
            print("Phone number cannot be empty.")
            return

        if email == "":
            print("Email cannot be empty.")
            return

        for contact in self.contacts:
            if contact["name"].lower() == name.lower():

                contact["phone"] = phone
                contact["email"] = email

                print("Contact updated successfully.")
                return

        print("Contact not found.")

    def list_contacts(self):

        if len(self.contacts) == 0:
            print("No contacts available.")
            return

        print("\n Contact List")

        for contact in self.contacts:
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])


manager = ContactManager()

while True:
    print("\n1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. List Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")

        manager.add_contact(name, phone, email)

    elif choice == "2":
        name = input("Enter name to delete: ")
        manager.delete_contact(name)

    elif choice == "3":
        name = input("Enter name to search: ")
        manager.search_contact(name)

    elif choice == "4":
        name = input("Enter name to update: ")
        phone = input("Enter new phone: ")
        email = input("Enter new email: ")

        manager.update_contact(name, phone, email)

    elif choice == "5":
        manager.list_contacts()

    elif choice == "6":
        print("exit done")
        break

    else:

        print("Invalid choice. Enter valid option")