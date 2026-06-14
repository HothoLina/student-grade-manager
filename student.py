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