import json
import os


FILE_NAME = "contact.json"

# file se data load karna
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {}

# file me data save karna
def save_contacts(contact):
    with open(FILE_NAME, "w") as f:
        json.dump(contact, f, indent=4)

# naya contact add karna
def add_contact(contact):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contact[name] = {"phone": phone, "email": email}
    print("Contact added successfully!")

# sab contacts dekhna
def view_contacts(contact):
    if not contact:
        print("No contacts found.")
    else:
        for name, info in contact.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

# search karna
def search_contact(contact):
    search = input("Enter name to search: ")
    if search in contact:
        print(contact[search])
    else:
        print("Not found")

# delete karna
def delete_contact(contact):
    delete = input("Enter name to delete: ")
    if delete in contact:
        del contact[delete]
        print("Contact deleted successfully!")
    else:
        print("Not found, delete nahi hua")

# main function
def main():
    contact = load_contacts()

    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contact)
        elif choice == "2":
            view_contacts(contact)
        elif choice == "3":
            search_contact(contact)
        elif choice == "4":
            delete_contact(contact)
        elif choice == "5":
            save_contacts(contact)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
