from db import create_tables
from student import add_student, view_students

create_tables()

print("===== Student Grade Manager =====")
print("1. Add Student")
print("2. View Students")
print("3. Exit")

choice = input("Choose: ")

if choice == "1":
    name = input("Enter name: ")
    email = input("Enter email: ")

    add_student(name, email)

    print("✅ Student added successfully!")

elif choice == "2":
    students = view_students()

    print("\nStudents:")
    for student in students:
        print(student)

elif choice == "3":
    print("Goodbye!")