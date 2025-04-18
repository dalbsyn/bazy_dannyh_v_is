#Вариант 3
import psycopg2

DB_PARAMS = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "1534",
    "host": "localhost",
    "port": "5432"
}

class Library:
    def __init__(self):
        self.conn = psycopg2.connect(**DB_PARAMS)
        self.cur = self.conn.cursor()

    def get_books(self):
        self.cur.execute("SELECT id, title, author, genre FROM books")
        return self.cur.fetchall()

    def get_loans(self):
        self.cur.execute("""
            SELECT loans.id, books.title, borrower, date_issued, date_due
            FROM loans
            JOIN books ON loans.book_id = books.id
        """)
        return self.cur.fetchall()

    def add_loan(self, book_id, borrower, date_issued, date_due):
        self.cur.execute("""
            INSERT INTO loans (book_id, borrower, date_issued, date_due)
            VALUES (%s, %s, %s, %s)
        """, (book_id, borrower, date_issued, date_due))
        self.conn.commit()

    def delete_loan(self, loan_id):
        self.cur.execute("DELETE FROM loans WHERE id = %s", (loan_id,))
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()

if __name__ == "__main__":
    db = Library()
    print("Книги:", db.get_books())
    print("Выдачи:", db.get_loans())
    db.close()
