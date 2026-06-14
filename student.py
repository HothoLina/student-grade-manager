from db import get_connection


def add_student(name, email):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO students (name, email)
    VALUES (%s, %s)
    """

    cursor.execute(query, (name, email))
    connection.commit()

    cursor.close()
    connection.close()


def view_students():
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM students"

    cursor.execute(query)

    students = cursor.fetchall()

    cursor.close()
    connection.close()

    return students


def search_student(name):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT * FROM students
    WHERE name LIKE %s
    """

    cursor.execute(query, (f"%{name}%",))

    students = cursor.fetchall()

    cursor.close()
    connection.close()

    return students


def delete_student(student_id):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    DELETE FROM students
    WHERE id = %s
    """

    cursor.execute(query, (student_id,))
    connection.commit()

    cursor.close()
    connection.close()


def update_student(student_id, name, email):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    UPDATE students
    SET name = %s,
        email = %s
    WHERE id = %s
    """

    cursor.execute(query, (name, email, student_id))
    connection.commit()

    cursor.close()
    connection.close()