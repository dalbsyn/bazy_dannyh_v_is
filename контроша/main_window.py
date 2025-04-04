8 вариант

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QTableWidget, QTableWidgetItem
from data_accessor import get_students_with_grades

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Студенты и их оценок")
        layout = QVBoxLayout(self)

self.student_select = QComboBox()
        self.student_select.currentIndexChanged.connect(self.load_grades)
        layout.addWidget(self.student_select)

        