#Вариант 3

# main_window.py
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QListWidget, QTableWidget,
    QTableWidgetItem, QPushButton, QHBoxLayout, QMessageBox
)
from data_accessor import LibraryDB
from datetime import date, timedelta

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Управление библиотекой")
        self.db = LibraryDB()

        layout = QVBoxLayout(self)

        #список
        self.book_list = QListWidget()
        self.load_books()
        layout.addWidget(self.book_list)

        #выдачи
        self.loan_table = QTableWidget()
        self.loan_table.setColumnCount(4)
        self.loan_table.setHorizontalHeaderLabels(["Книга", "Читатель", "Дата выдачи", "Срок до"])
        layout.addWidget(self.loan_table)
        self.load_loans()

        #кнопки
        button_layout = QHBoxLayout()
        self.issue_button = QPushButton("Выдать книгу")
        self.return_button = QPushButton("Принять возврат")
        self.issue_button.clicked.connect(self.issue_book)
        self.return_button.clicked.connect(self.return_book)
        button_layout.addWidget(self.issue_button)
        button_layout.addWidget(self.return_button)
        layout.addLayout(button_layout)

    def load_books(self):
        self.books = self.db.get_books()
        self.book_list.clear()
        for book in self.books:
            self.book_list.addItem(f"{book[1]} — {book[2]}")  # Название — Автор

    def load_loans(self):
        self.loans = self.db.get_loans()
        self.loan_table.setRowCount(len(self.loans))
        for row, loan in enumerate(self.loans):
            for col in range(1, 5):
                item = QTableWidgetItem(str(loan[col - 1]))
                self.loan_table.setItem(row, col - 1, item)

    def issue_book(self):
        selected = self.book_list.currentRow()
        if selected == -1:
            QMessageBox.warning(self, "Ошибка", "Выберите книгу для выдачи")
            return
        book_id = self.books[selected][0]
        borrower = "Читатель"  # Просто пример, можно добавить ввод
        today = date.today()
        due = today + timedelta(days=14)
        self.db.add_loan(book_id, borrower, today, due)
        self.load_loans()

    def return_book(self):
        selected = self.loan_table.currentRow()
        if selected == -1:
            QMessageBox.warning(self, "Ошибка", "Выберите выдачу для возврата")
            return
        loan_id = self.loans[selected][0]
        self.db.delete_loan(loan_id)
        self.load_loans()

    def closeEvent(self, event):
        self.db.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
