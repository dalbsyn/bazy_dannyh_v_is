from PySide6.QtWidgets import (QWidget, QTableWidgetItem, QLabel, QPushButton, QFormLayout, QTableWidget, QVBoxLayout, QApplication, QLineEdit)
from data_accessor import DataAccessor


class Table(QTableWidget):
    def __init__(self):
        super().__init__()
        self.data_accessor = DataAccessor()

    def fill_table(self):
        self.result = self.data_accessor.get_table()


class StudentCourse(QFormLayout):
    def __init__(self):
        super().__init__()
        self.init_widgets()
        self.add_widgets()

    def init_widgets(self):
        self.label_student = QLabel('Студент:')
        self.label_course = QLabel('Курс:')
        self.line_student = QLineEdit()
        self.line_course = QLineEdit()

    def add_widgets(self):
        self.addRow(self.label_student, self.line_student)
        self.addRow(self.label_course, self.line_course)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_layout()
        self.init_widgets()
        self.add_widgets()

    def init_layout(self):
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

    def init_widgets(self):
        self.table = Table()
        self.student_course = StudentCourse()
        self.button_add = QPushButton('Добавить')
        self.button_delete = QPushButton('Удалить')

    def add_widgets(self):
        self.main_layout.addWidget(self.table)
        self.main_layout.addLayout(self.student_course)
        self.main_layout.addWidget(self.button_add)
        self.main_layout.addWidget(self.button_delete)


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
