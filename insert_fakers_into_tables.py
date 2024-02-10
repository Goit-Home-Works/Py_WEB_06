from faker import Faker
import random
from psycopg2 import connect, extensions, Error
from create_tables_postgresql import create_tables 

def insert_fake_data(conn):
    fake = Faker()

    # Create tables
    create_tables(conn)

    # Insert fake data
    with conn.cursor() as cur:
        # Groups
        groups = [f"Group {i+1}" for i in range(3)]
        for group in groups:
            cur.execute("INSERT INTO groups (name) VALUES (%s)", (group,))

        # Teachers
        teachers = [fake.name() for _ in range(5)]
        cur.executemany(
            "INSERT INTO teachers (name) VALUES (%s)",
            [(teacher,) for teacher in teachers],
        )

        # Subjects
        subjects = [
            (fake.word(), random.choice(range(1, 6))) for _ in range(8)
        ]  # Assign a random teacher to each subject
        cur.executemany(
            "INSERT INTO subjects (subject_name, teacher_id) VALUES (%s, %s)", subjects
        )

        # Students
        students = [
            (fake.name(), random.choice(range(1, 4))) for _ in range(30)
        ]  # Assign a random group to each student
        cur.executemany(
            "INSERT INTO students (name, group_id) VALUES (%s, %s)", students
        )

        # Grades
        grades = [
            (
                random.randint(60, 100),
                fake.date_time_this_year(before_now=True, after_now=False),
                random.choice(range(1, 31)),
                random.choice(range(1, 9)),
            )
            for _ in range(20)
        ]
        cur.executemany(
            "INSERT INTO grades (value, date, student_id, subject_id) VALUES (%s, %s, %s, %s)",
            grades,
        )

        # Commit changes to the database
        conn.commit()


if __name__ == "__main__":

    try:
        # Connect to the PostgreSQL server
        conn = connect(
            user="your_username",
            password="your_password",
            host="localhost",
            port="5432",
            dbname="your_database_name",
        )

        # Insert fake data
        insert_fake_data(conn)

    except Error as e:
        print(f"Error connecting to PostgreSQL: {e}")

    finally:
        # Close the connection
        if conn:
            conn.close()
