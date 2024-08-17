# from PyQt6.QtWidgets import QApplication, QWidget # PyQt6 having issues
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtCore import QSize, Qt

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!!")

        self.setCentralWidget(button)

app = QApplication(sys.argv)

# window = QWidget()
# window = QPushButton("Push Me!!")
# window = QMainWindow()
window = MainWindow()
window.show()

app.exec()