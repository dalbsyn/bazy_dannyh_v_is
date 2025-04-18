import psycopg2

class DataAccessor:
    def __init__(self):
        db_parameters = {
            "dbname": "Kontrol_rabota",
            "user": "postgres",
            "password": "QweAsd12345@"
        }
        self.connection = psycopg2.connect(**db_parameters)
        self.cursor = self.connection.cursor()

    def add_booking(self, room_id, guest_name, check_in, check_out):
        self.cursor.execute(
            "INSERT INTO bookings (room_id, guest_name, check_in, check_out) VALUES (%s, %s, %s, %s)",
            (room_id, guest_name, check_in, check_out)
        )
        self.connection.commit()

    def delete_booking(self, booking_id):
        self.cursor.execute("DELETE FROM bookings WHERE id = %s", (booking_id,))
        self.connection.commit()

    def get_bookings_by_room(self, room_id):
        self.cursor.execute(
            "SELECT id, guest_name, check_in, check_out FROM bookings WHERE room_id = %s ORDER BY check_in",
            (room_id,)
        )
        return self.cursor.fetchall()

    def get_available_rooms(self):
        self.cursor.execute("SELECT id, room_number, type, price FROM rooms ORDER BY room_number")
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()

if __name__ == "__main__":
    db = DataAccessor()
    available_rooms = db.get_available_rooms()
    print("Доступные номера:", available_rooms)


    # db.add_booking(1, "Иванов И.И.", "2025-04-20", "2025-04-25")


    # bookings = db.get_bookings_by_room(1)
    # print(bookings)

    db.close()