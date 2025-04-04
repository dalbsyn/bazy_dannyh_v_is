#7вариант
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
    CREATE TABLE IF NOT EXISTS rooms (
        id SERIAL PRIMARY KEY,
        number VARCHAR(10),
        type VARCHAR(50),
        price_per_night NUMERIC
    )
    """)

cur.execute("""
    CREATE TABLE IF NOT EXISTS reservations (
	id SERIAL PRIMARY KEY,
	room_id INT REFERENCES rooms(id),
        guest_name VARCHAR(30),
        check_in DATE,
        check_out DATE
    )
    """)

cur.execute("""
    INSERT INTO rooms (number, type, price_per_night) VALUES
    ('101', 'Одноместный', 10000),
    ('102', 'Двухместный', 15000),
    ('201', 'Люкс', 25000)
    """)

cur.execute("""
    INSERT INTO reservations (room_id, guest_name, check_in, check_out) VALUES
    (1, 'Иван Соколов', '2025-04-01', '2025-04-05'),
    (2, 'Анна Смирнова', '2025-04-03', '2025-04-06')
    """)

conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_tables()




