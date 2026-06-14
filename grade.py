from db import get_connection


def add_grade(student_id, subject, grade):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO grades (student_id, subject, grade)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (student_id, subject, grade))
    connection.commit()

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