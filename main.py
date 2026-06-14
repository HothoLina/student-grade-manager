from db import create_tables
from student import (
    add_student,
    view_students,
    search_student,
    delete_student,
    update_student
)
from grade import (
    add_grade,
    view_student_grades,
    calculate_average,
    generate_report
)
from tabulate import tabulate

create_tables()

while True:

    print("\n===== Student Grade Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Add Grade")
    print("5. View Student Grades")
    print("6. Calculate Average")
    print("7. Delete Student")
    print("8. Update Student")
    print("9. Student Report")
    print("10. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter name: ")
        email = input("Enter email: ")

        add_student(name, email)

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
        student_id = input("Enter Student ID: ")
        subject = input("Enter Subject: ")

        try:
            grade = float(input("Enter Grade: "))
        except:
            print("❌ Invalid grade format!")
            continue

        add_grade(student_id, subject, grade)

    elif choice == "5":
        student_id = input("Enter Student ID: ")

        grades = view_student_grades(student_id)

        if grades:
            print(tabulate(
                grades,
                headers=["Grade ID", "Subject", "Grade"],
                tablefmt="grid"
            ))
        else:
            print("No grades found.")

    elif choice == "6":
        student_id = input("Enter Student ID: ")

        average = calculate_average(student_id)

        if average is not None:
            print(f"\n📊 Average Grade: {average:.2f}")
        else:
            print("No grades found.")

    elif choice == "7":
        student_id = input("Enter Student ID to delete: ")

        delete_student(student_id)

        print("✅ Student deleted successfully!")

    elif choice == "8":
        student_id = input("Enter Student ID: ")
        name = input("Enter New Name: ")
        email = input("Enter New Email: ")

        update_student(student_id, name, email)

        print("✅ Student updated successfully!")

    elif choice == "9":
        student_id = input("Enter Student ID: ")

        report = generate_report(student_id)

        if report is None:
            print("Student not found.")
            continue

        print("\n===== STUDENT REPORT =====")
        print(f"Name: {report['name']}")
        print(f"Email: {report['email']}")

        print("\nSubjects:")

        print(tabulate(
            report["grades"],
            headers=["Subject", "Grade"],
            tablefmt="grid"
        ))

        average = report["average"]

        if average is not None:
            print(f"\nAverage Grade: {average:.2f}")

            if average >= 90:
                performance = "Excellent"
            elif average >= 80:
                performance = "Very Good"
            elif average >= 70:
                performance = "Good"
            elif average >= 60:
                performance = "Pass"
            else:
                performance = "Needs Improvement"

            print(f"Performance: {performance}")

    elif choice == "10":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please try again.")