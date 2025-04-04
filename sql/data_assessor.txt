#7вариант
import psycopg2

DB_PARAMS = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "1534",
    "host": "localhost",
    "port": "5432"
}
	
def get_rooms():
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute("SELECT id, number, type, price_per_night FROM rooms")
    rooms = cur.fetchall()
    conn.close()
    return rooms

def get_reservations():
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute("""
        SELECT reservations.id, rooms.number, guest_name, check_in, check_out
        FROM reservations
        JOIN rooms ON reservations.room_id = rooms.id
    """)
    reservations = cur.fetchall()
    conn.close()
    return reservations

def add_reservation(room_id, guest_name, check_in, check_out):
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO reservations (room_id, guest_name, check_in, check_out)
        VALUES (%s, %s, %s, %s)
    """, (room_id, guest_name, check_in, check_out))
    conn.commit()
    cur.close()
    conn.close()

def delete_reservation(reservation_id):
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute("DELETE FROM reservations WHERE id = %s", (reservation_id,))
    conn.commit()
    cur.close()
    conn.close()
