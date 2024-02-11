from faker import Faker
from faker.providers import DynamicProvider
import random
from psycopg2 import connect, extensions, Error


def insert_fake_data(conn):
    fake = Faker()

    subjects_provider = DynamicProvider(
        provider_name="study_subjects",
        elements=[
            "App development",
            "Computer programming",
            "Computer repair",
            "Graphic design",
            "Media technology",
            "Video game development",
            "Web design",
            "Web programming",
        ],
    )
    fake.add_provider(subjects_provider)

    # Insert fake data
    with conn.cursor() as cur:
        
        # Groups
        
        # groups = [i+1 for i in range(3)]
        # for group in groups:
        #     cur.execute("INSERT INTO groups (id, name) VALUES (%s, %s)", (group, group))

        # # Teachers
        
        # teachers = [
        #     (i, fake.name(), ) for i in range(1, 6)  # Start from 1 to match teacher_id
        # ]

        # cur.executemany(
        #     "INSERT INTO teachers (id, teacher_name) VALUES (%s, %s)",
        #     teachers,
        # )

        # # Subjects
        
        # subjects = [(i+1, fake.study_subjects(), random.choice(range(1, 6))) for i in range(8)]
        # cur.executemany(
        #     "INSERT INTO subjects (id, subject_name, teacher_id) VALUES (%s, %s, %s)", subjects
        # )


        # # Students
        
        # students = [
        #     (i+1, fake.name(),  random.choice(range(1, 4))) for i in range(30)
        # ]  # Assign a random group to each student
        # cur.executemany(
        #     "INSERT INTO students (id, name, group_id) VALUES (%s, %s, %s)", students
        # )

        # Grades
        
        # Fetch student IDs from the database
        cur.execute("SELECT id FROM students")
        student_ids = [row[0] for row in cur.fetchall()]

        # Fetch subject IDs from the database
        cur.execute("SELECT id FROM subjects")
        subject_ids = [row[0] for row in cur.fetchall()]

        # Generate grades for each student and subject with a minimum of 4 grades
        grades = []

        for student_id in student_ids:
            for subject_id in subject_ids:
                # Ensure each student has a minimum of 4 grades for each subject
                for _ in range(4):
                    grade = (
                        random.randint(60, 100),
                        fake.date_time_this_year(before_now=True, after_now=False),
                        student_id,
                        subject_id,
                    )
                    grades.append(grade)

        # Insert grades into the database
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
            dbname="postgres",
            user="postgres",
            password="sergio",
            host="localhost",
            port=5432,
        )

        # Insert fake data
        insert_fake_data(conn)

    except Error as e:
        print(f"Error connecting to PostgreSQL: {e}")

    finally:
        # Close the connection
        if conn:
            conn.close()
