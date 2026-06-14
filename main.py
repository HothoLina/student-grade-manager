from db import create_tables
from student import add_student, view_students, search_student
from grade import add_grade, view_student_grades
from tabulate import tabulate

create_tables()

print("===== Student Grade Manager =====")
print("1. Add Student")
print("2. View Students")
print("3. Search Student")
print("4. Add Grade")
print("5. View Student Grades")
print("6. Exit")

choice = input("Choose: ")

if choice == "1":
    name = input("Enter name: ")
    email = input("Enter email: ")

    add_student(name, email)

    print("✅ Student added successfully!")

elif choice == "2":
    students = view_students()

    if students:
        print(tabulate(
            students,
            headers=["ID", "Name", "Email"],
            tablefmt="grid"
        ))
    else:
        print("No students found.")

elif choice == "3":
    name = input("Enter student name: ")

    students = search_student(name)

    if students:
        print(tabulate(
            students,
            headers=["ID", "Name", "Email"],
            tablefmt="grid"
        ))
    else:
        print("No matching students found.")

elif choice == "4":
    student_id = int(input("Enter Student ID: "))
    subject = input("Enter Subject: ")
    grade = float(input("Enter Grade: "))

    add_grade(student_id, subject, grade)

    print("✅ Grade added successfully!")

elif choice == "5":
    student_id = int(input("Enter Student ID: "))

    grades = view_student_grades(student_id)

    if grades:
        print(tabulate(
            grades,
            headers=["Grade ID", "Subject", "Grade"],
            tablefmt="grid"
        ))
    else:
        print("No grades found for this student.")

elif choice == "6":
    print("Goodbye!")