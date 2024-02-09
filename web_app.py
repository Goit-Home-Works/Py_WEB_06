from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/grades')
def grades():
    conn = psycopg2.connect(user='postgres', password='12345', host='localhost', port='5432', dbname='postgres')
    cur = conn.cursor()

    cur.execute('SELECT * FROM grades')
    grades = cur.fetchall()

    cur.close()
    conn.close()


    return render_template('grades.html', grades=grades)

@app.route('/groups')
def groups():
    conn = psycopg2.connect(user='postgres', password='12345', host='localhost', port='5432', dbname='postgres')
    cur = conn.cursor()

    cur.execute('SELECT * FROM groups')
    groups = cur.fetchall()

    cur.close()
    conn.close()


    return render_template('groups.html', groups=groups)

@app.route('/students')
def students():
    conn = psycopg2.connect(user='postgres', password='12345', host='localhost', port='5432', dbname='postgres')
    cur = conn.cursor()

    cur.execute('SELECT * FROM students')
    students = cur.fetchall()

    cur.close()
    conn.close()


    return render_template('students.html', students=students)

@app.route('/subjects')
def subjects():
    conn = psycopg2.connect(user='postgres', password='12345', host='localhost', port='5432', dbname='postgres')
    cur = conn.cursor()

    cur.execute('SELECT * FROM subjects')
    subjects = cur.fetchall()

    cur.close()
    conn.close()


    return render_template('subjects.html',subjects=subjects)

@app.route('/teachers')
def teachers():
    conn = psycopg2.connect(user='postgres', password='12345', host='localhost', port='5432', dbname='postgres')
    cur = conn.cursor()

    cur.execute('SELECT * FROM teachers')
    teachers = cur.fetchall()

    cur.close()
    conn.close()


    return render_template('teachers.html', teachers=teachers)


if __name__ == '__main__':
    app.run(debug=True)
