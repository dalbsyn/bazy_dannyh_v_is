#7вариант
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListView, QLabel, QLineEdit, QFormLayout, QComboBox
from PySide6.QtCore import QStringListModel
from data_accessor import get_rooms, get_reservations, add_reservation, delete_reservation

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Бронирование номеров в отеле")