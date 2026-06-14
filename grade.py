from db import get_connection


def add_grade(student_id, subject, grade):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
        SELECT id FROM students WHERE id = %s
        """, (student_id,))

        student = cursor.fetchone()

        if not student:
            print("❌ Error: Student ID does not exist!")
            return

        cursor.execute("""
        INSERT INTO grades (student_id, subject, grade)
        VALUES (%s, %s, %s)
        """, (student_id, subject, grade))

        connection.commit()
        print("✅ Grade added successfully!")

    except Exception as e:
        print("❌ Error:", e)

    finally:
        cursor.close()
        connection.close()


def view_student_grades(student_id):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT id, subject, grade
    FROM grades
    WHERE student_id = %s
    """

    cursor.execute(query, (student_id,))
    grades = cursor.fetchall()

    cursor.close()
    connection.close()

    return grades


def calculate_average(student_id):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
        SELECT AVG(grade)
        FROM grades
        WHERE student_id = %s
        """, (student_id,))

        result = cursor.fetchone()[0]

        return result

    except Exception as e:
        print("❌ Error:", e)
        return None

    finally:
        cursor.close()
        connection.close()


def generate_report(student_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT name, email
        FROM students
        WHERE id = %s
    """, (student_id,))

    student = cursor.fetchone()

    if not student:
        cursor.close()
        connection.close()
        return None

    cursor.execute("""
        SELECT subject, grade
        FROM grades
        WHERE student_id = %s
    """, (student_id,))

    grades = cursor.fetchall()

    cursor.execute("""
        SELECT AVG(grade)
        FROM grades
        WHERE student_id = %s
    """, (student_id,))

    average = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return {
        "name": student[0],
        "email": student[1],
        "grades": grades,
        "average": average
    }