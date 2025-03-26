from PySide6.QtWidgets import QGridLayout, QApplication, QLabel, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.layout_main = QGridLayout()
        self.setLayout(self.layout_main)
        self.label_main = QLabel('Текст')
        self.layout_main.addWidget(self.label_main, 0, 0)
        self.setWindowTitle('Заголовок')
        self.setMinimumWidth(200)

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()