#Вариант 3
import psycopg2

DB_PARAMS = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "1534",
    "host": "localhost",
    "port": "5432"
}

def create_tables():
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id SERIAL PRIMARY KEY,
            title VARCHAR(100),
            author VARCHAR(100),
            genre VARCHAR(50)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS loans (
            id SERIAL PRIMARY KEY,
            book_id INT REFERENCES books(id),
            borrower VARCHAR(100),
            date_issued DATE,
            date_due DATE
        )
    """)

    cur.execute("""
        INSERT INTO books (title, author, genre) VALUES
        ('Зеленая Миля', 'Стивен Кинг', 'Триллер'),
        ('Хроники Нарнии', 'Клайв Льюис', 'Фантастика'),
        ('Гарри Поттер', 'Джоан Роулинг', 'Фантастика')
    """)

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_tables()
