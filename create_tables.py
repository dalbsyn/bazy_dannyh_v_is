import psycopg2

db_params = {
    "dbname": "Kontrol_rabota",
    "user": "postgres",
    "password": "QweAsd12345@"
}

connection = psycopg2.connect(**db_params)
cursor = connection.cursor()

def create_tables(cursor):
    cursor.execute("""
        DROP TABLE IF EXISTS bookings;
        DROP TABLE IF EXISTS rooms;

        CREATE TABLE rooms (
            id SERIAL PRIMARY KEY,
            room_number VARCHAR(10) NOT NULL,
            type VARCHAR(50),
            price INTEGER
        );

        CREATE TABLE bookings (
            id SERIAL PRIMARY KEY,
            room_id INTEGER REFERENCES rooms(id) ON DELETE CASCADE,
            guest_name VARCHAR(100) NOT NULL,
            check_in DATE NOT NULL,
            check_out DATE NOT NULL
        );
    """)
    connection.commit()


    cursor.execute("""
        INSERT INTO rooms (room_number, type, price) VALUES
        ('101', 'Single', 3000),
        ('102', 'Double', 4500),
        ('201', 'Suite', 8000)
    """)
    connection.commit()

    cursor.close()
    connection.close()

if __name__ == "__main__":
    create_tables(cursor)