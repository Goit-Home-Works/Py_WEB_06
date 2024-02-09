import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Connect to SQLite
conn = sqlite3.connect('hw_06_sqlite.db')

# Create a cursor object to interact with the database
cur = conn.cursor()

# Create tables

# Groups
cur.execute('''
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
''')

# Students
cur.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        group_id INTEGER REFERENCES groups(id)
    )
''')

# Teachers
cur.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
''')

# Subjects
cur.execute('''
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        teacher_id INTEGER REFERENCES teachers(id)
    )
''')

# Grades
cur.execute('''
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY,
        value INTEGER NOT NULL,
        date TEXT DEFAULT CURRENT_TIMESTAMP,
        student_id INTEGER REFERENCES students(id),
        subject_id INTEGER REFERENCES subjects(id)
    )
''')

# Commit changes to the database
conn.commit()

# Generate random data and fill tables

# Groups
groups = [f'Group {i+1}' for i in range(3)]
cur.executemany('INSERT INTO groups (name) VALUES (?)', [(group,) for group in groups])

# Teachers
teachers = [fake.name() for _ in range(5)]
cur.executemany('INSERT INTO teachers (name) VALUES (?)', [(teacher,) for teacher in teachers])

# Subjects
subjects = [(fake.word(), random.choice(range(1, 6))) for _ in range(8)]  # Assign a random teacher to each subject
cur.executemany('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', subjects)

# Students
students = [(fake.name(), random.choice(range(1, 4))) for _ in range(30)]  # Assign a random group to each student
cur.executemany('INSERT INTO students (name, group_id) VALUES (?, ?)', students)

# Grades
grades = [(random.randint(60, 100), fake.date_time_this_year(before_now=True, after_now=False).strftime('%Y-%m-%d %H:%M:%S'), random.choice(range(1, 31)), random.choice(range(1, 9))) for _ in range(20)]
cur.executemany('INSERT INTO grades (value, date, student_id, subject_id) VALUES (?, ?, ?, ?)', grades)

# Commit changes to the database
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
