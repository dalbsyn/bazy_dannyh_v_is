8 вариант 

import psycopg2

DB_PARAMS = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "123",
    "host": "localhost",
    "port": "5432",
}

def get_students_with_grades():
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute("""
    SELECT students.id, students.name, students.group_name, grades.subject, grades.grade
    FROM students
    LEFT JOIN grades ON students.id = grades.student_id
    """)
    students = cur.fetchall()
    cur.close()
    conn.close()
    return students

def add_grade(student_id, subject, grade):
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO grades (student_id, subject, grade) VALUES (%s, %s, %s)
    """, (student_id, subject, grade))
    conn.commit()
    cur.close()
    conn.close()

def delete_grade(grade_id):
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute("DELETE FROM grades WHERE id = %s", (grade_id,))
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    print(get_students_with_grades())

       