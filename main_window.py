from PySide6.QtWidgets import (
    QVBoxLayout, QWidget, QApplication, QLineEdit, QFormLayout,
    QPushButton, QTableWidget, QTableWidgetItem, QListWidget, QMessageBox, QHBoxLayout
)
from data_accessor import DataAccessor
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Бронирование номеров в отеле")
        self.setGeometry(150, 150, 900, 500)

        self.data_accessor = DataAccessor()


        layout = QVBoxLayout()

     
        self.room_list = QListWidget()
        self.room_list.itemClicked.connect(self.load_bookings_for_room)
        layout.addWidget(self.room_list)


        self.booking_table = QTableWidget(0, 4)
        self.booking_table.setHorizontalHeaderLabels(["ID", "Гость", "Дата въезда", "Дата выезда"])
        layout.addWidget(self.booking_table)

        form_layout = QFormLayout()
        self.guest_name = QLineEdit()
        self.check_in = QLineEdit()
        self.check_out = QLineEdit()
        self.booking_id_delete = QLineEdit()

        form_layout.addRow("Имя гостя:", self.guest_name)
        form_layout.addRow("Дата въезда (YYYY-MM-DD):", self.check_in)
        form_layout.addRow("Дата выезда (YYYY-MM-DD):", self.check_out)
        form_layout.addRow("ID брони для отмены:", self.booking_id_delete)

        layout.addLayout(form_layout)

     
        button_layout = QHBoxLayout()
        self.add_booking_btn = QPushButton("Забронировать")
        self.add_booking_btn.clicked.connect(self.add_booking)
        self.delete_booking_btn = QPushButton("Отменить бронирование")
        self.delete_booking_btn.clicked.connect(self.delete_booking)
        button_layout.addWidget(self.add_booking_btn)
        button_layout.addWidget(self.delete_booking_btn)

        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.load_rooms()

    def load_rooms(self):
        self.room_list.clear()
        rooms = self.data_accessor.get_available_rooms()
        for room in rooms:
            self.room_list.addItem(f"{room[0]} - Номер {room[1]} | {room[2]} | {room[3]} руб.")

    def load_bookings_for_room(self):
        selected = self.room_list.currentItem()
        if selected:
            room_id = int(selected.text().split(" - ")[0])
            self.current_room_id = room_id
            bookings = self.data_accessor.get_bookings_by_room(room_id)
            self.booking_table.setRowCount(0)
            for row_index, booking in enumerate(bookings):
                self.booking_table.insertRow(row_index)
                for col_index, value in enumerate(booking):
                    self.booking_table.setItem(row_index, col_index, QTableWidgetItem(str(value)))

    def add_booking(self):
        if not hasattr(self, "current_room_id"):
            QMessageBox.warning(self, "Ошибка", "Сначала выберите номер!")
            return

        guest_name = self.guest_name.text()
        check_in = self.check_in.text()
        check_out = self.check_out.text()

        self.data_accessor.add_booking(self.current_room_id, guest_name, check_in, check_out)
        self.load_bookings_for_room()

    def delete_booking(self):
        try:
            booking_id = int(self.booking_id_delete.text())
            self.data_accessor.delete_booking(booking_id)
            self.load_bookings_for_room()
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Введите корректный ID для удаления.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())