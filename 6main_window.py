import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from db import get_connection

class CarApp(QWidget):
    def _init_(self):
        super()._init_()

        self.setWindowTitle("Учёт автомобилей")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        # Форма для добавления владельца
        form_layout = QFormLayout()
        self.name_input = QLineEdit()
        self.birth_date_input = QLineEdit()
        form_layout.addRow("Имя владельца:", self.name_input)
        form_layout.addRow("Дата рождения:", self.birth_date_input)

        self.add_owner_btn = QPushButton("Добавить владельца")
        self.add_owner_btn.clicked.connect(self.add_owner)

        # Таблица автомобилей
        self.car_table = QTableWidget(0, 4)
        self.car_table.setHorizontalHeaderLabels(["ID", "Владелец", "Марка", "Модель", "Год"])

        # Кнопки
        self.load_cars_btn = QPushButton("Обновить список автомобилей")
        self.load_cars_btn.clicked.connect(self.load_cars)

        layout.addLayout(form_layout)
        layout.addWidget(self.add_owner_btn)
        layout.addWidget(self.car_table)
        layout.addWidget(self.load_cars_btn)

        self.setLayout(layout)

    def add_owner(self):
        name = self.name_input.text()
        birth_date = self.birth_date_input.text()

        conn = get_connection()
        if conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO owners (name, birth_date) VALUES (%s, %s)", (name, birth_date))
                conn.commit()
            conn.close()

    def load_cars(self):
        conn = get_connection()
        if conn:
            with conn.cursor() as cur:
                cur.execute("SELECT cars.id, owners.name, cars.brand, cars.model, cars.year FROM cars JOIN owners ON cars.owner_id = owners.id")
                rows = cur.fetchall()
                self.car_table.setRowCount(len(rows))

                for row_idx, row in enumerate(rows):
                    for col_idx, value in enumerate(row):
                        self.car_table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

            conn.close()

if _name_ == "_main_":
    app = QApplication(sys.argv)
    window = CarApp()
    window.show()
    sys.exit(app.exec())