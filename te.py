# import json
# import os


# FILE_NAME = "contact.json"

# # file se data load karna
# def load_contacts():
#     if os.path.exists(FILE_NAME):
#         with open(FILE_NAME, "r") as f:
#             return json.load(f)
#     return {}

# # file me data save karna
# def save_contacts(contact):
#     with open(FILE_NAME, "w") as f:
#         json.dump(contact, f, indent=4)

# # naya contact add karna
# def add_contact(contact):
#     name = input("Enter name: ")
#     phone = input("Enter phone: ")
#     email = input("Enter email: ")
#     contact[name] = {"phone": phone, "email": email}
#     print("Contact added successfully!")

# # sab contacts dekhna
# def view_contacts(contact):
#     if not contact:
#         print("No contacts found.")
#     else:
#         for name, info in contact.items():
#             print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

# # search karna
# def search_contact(contact):
#     search = input("Enter name to search: ")
#     if search in contact:
#         print(contact[search])
#     else:
#         print("Not found")

# # delete karna
# def delete_contact(contact):
#     delete = input("Enter name to delete: ")
#     if delete in contact:
#         del contact[delete]
#         print("Contact deleted successfully!")
#     else:
#         print("Not found, delete nahi hua")

# # main function
# def main():
#     contact = load_contacts()

#     while True:
#         print("\n--- Contact Book ---")
#         print("1. Add Contact")
#         print("2. View Contacts")
#         print("3. Search Contact")
#         print("4. Delete Contact")
#         print("5. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             add_contact(contact)
#         elif choice == "2":
#             view_contacts(contact)
#         elif choice == "3":
#             search_contact(contact)
#         elif choice == "4":
#             delete_contact(contact)
#         elif choice == "5":
#             save_contacts(contact)
#             print("Data saved. Exiting...")
#             break
#         else:
#             print("Invalid choice! Please try again.")

# if __name__ == "__main__":
#     main()

# from datetime  import datetime
# import time
# while True:
#     k = datetime.now()
#     hours = k.hour
#     mint = k.minute
#     scd = k.second

#     yourstime = (f"this is your hours{hours} this is your minute {mint} this is your second {scd}")

#     print(yourstime)
#     time.sleep(1.9 )

import random

#quiz game 

quiz = [
    
    {
        "question": "Python me timeit module ka use kya hai?",
        "options": [
            "1. Code ka execution time measure karne ke liye",
            "2. Real time clock",
            "3. Alarm set karne ke liye",
            "4. Thread sleep karne ke liye"
        ],
        "answer": "1"
    },
    {
        "question": "Python me __all__ variable module me kis liye hota hai?",
        "options": [
            "1. Public API define karne ke liye",
            "2. Memory allocate karne ke liye",
            "3. Error handle karne ke liye",
            "4. Logging"
        ],
        "answer": "1"
    },
    {
        "question": "Python me del statement kis liye hota hai?",
        "options": [
            "1. Object delete karne ke liye",
            "2. Memory increase karne ke liye",
            "3. Error raise karne ke liye",
            "4. Loop break karne ke liye"
        ],
        "answer": "1"
    },
    {
        "question": "Python me sys.getsizeof() function kya return karta hai?",
        "options": [
            "1. Object ka size (bytes me)",
            "2. List length",
            "3. File size",
            "4. String length"
        ],
        "answer": "1"
    },
    {
        "question": "Python me logging module ka default level kya hai?",
        "options": ["1. WARNING", "2. ERROR", "3. DEBUG", "4. INFO"],
        "answer": "1"
    },
    {
        "question": "Python me memory leak avoid karne ke liye kaunsa module useful hai?",
        "options": ["1. weakref", "2. gc", "3. memoryview", "4. sabhi"],
        "answer": "4"
    },
    {
        "question": "Python me __call__ method ka use kis liye hota hai?",
        "options": [
            "1. Object ko function ki tarah callable banana",
            "2. Function call karna",
            "3. Thread start karna",
            "4. Error raise karna"
        ],
        "answer": "1"
    },
    {
        "question": "Python me enumerate() function kya return karta hai?",
        "options": [
            "1. Index ke sath iterable",
            "2. Sirf index",
            "3. Sirf values",
            "4. Random values"
        ],
        "answer": "1"
    },
    {
        "question": "Python me zip() function kya karta hai?",
        "options": [
            "1. Multiple iterables ko tuple pairs me combine karta hai",
            "2. Files compress karta hai",
            "3. String join karta hai",
            "4. Random shuffle karta hai"
        ],
        "answer": "1"
    },
    {
        "question": "Python me assert statement kis liye hota hai?",
        "options": [
            "1. Condition test karne ke liye",
            "2. Loop break karne ke liye",
            "3. Memory allocate karne ke liye",
            "4. Logging"
        ],
        "answer": "1"
    }
]

import random

print("\n--- Welcome to Quiz Game ---")
score = 0

rnd = random.randint(0, len(quiz) - 1)
q = quiz[rnd]

# print(q)
print(q["question"])
for opt in q["options"]:
    print(opt)

ans = input("Enter your choice (1-4): ")
if ans == q["answer"]:
    print("✅ Correct!\n")
    score += 1
else:
    print("❌ Wrong Answer. Correct is:", q["answer"], "\n")

print(f"Your final score: {score}/1")
