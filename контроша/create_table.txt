8 вариант

import psycopg2

DB_PARAMS = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "123",
    "host": "localhost",
    "port": "5432",
}

def create_tables():
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS teachers (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        subject VARCHAR(255) NOT NULL
    );
    """)
 cur.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        teacher_id INT NOT NULL REFERENCES teachers(id)
    );
    """)

    conn.commit()
   INSERT INTO students (name, group_name) VALUES
    ('Иван Лукаш', 'Группа 1'),
    ('Татьяна Кузнецова', 'Группа 2'),
    ('Алексей Федотов', 'Группа 1')
    ON CONFLICT DO NOTHING;
    """)

cur.execute("""
    INSERT INTO grades (student_id, subject, grade) VALUES
    (1, 'Математика', 5),
    (1, 'История', 4),
    (2, 'Математика', 3),
    (2, 'Физика', 5),
    (3, 'Химия', 4)
    ON CONFLICT DO NOTHING;
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Таблицы успешно созданы и заполнены данными.")