# from PyQt6.QtWidgets import QApplication, QWidget # PyQt6 having issues
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QVBoxLayout
from PyQt5.QtCore import QSize, Qt

import sys
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.setWindowTitle("My App")
        dir = os.getcwd()
        buttons = [QPushButton(item, self) for item in os.listdir(dir) if os.path.isdir(item) and not item.startswith('.')]
        for button in buttons:
            button.clicked.connect(lambda ch, text=button.text(): print(text))
            # print(button.text())
            self.layout.addWidget(button)

        items = [item for item in os.listdir(dir) if os.path.isdir(item) and not item.startswith('.')]
        for item in items:
            newButton = QPushButton(item, self)
            newButton.clicked.connect(lambda ch, text=newButton.text(): print(text))
            # print(button.text())
            self.layout.addWidget(newButton)

        widget = QWidget()
        widget.setLayout(self.layout)

        self.setCentralWidget(widget)

        self.setFixedSize(QSize(400, 300))

app = QApplication(sys.argv)

# window = QWidget()
# window = QPushButton("Push Me!!")
# window = QMainWindow()
window = MainWindow()
window.show()

app.exec()