from db import create_tables
from student import add_student

create_tables()

print("===== Student Grade Manager =====")
print("1. Add Student")
print("2. Exit")

choice = input("Choose: ")

if choice == "1":
    name = input("Enter name: ")
    email = input("Enter email: ")

    add_student(name, email)

    print("✅ Student added successfully!")

elif choice == "2":
    print("Goodbye!")