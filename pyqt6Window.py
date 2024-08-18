# from PyQt6.QtWidgets import QApplication, QWidget # PyQt6 having issues
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QVBoxLayout, QLabel
from PyQt5.QtCore import QSize, Qt

import sys
import os

from createSilhouette import SilhouetteMaker

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.path = os.getcwd()
        self.dirButtons = QWidget()
        self.layout = QVBoxLayout(self.dirButtons)

        self.setWindowTitle("My App")
        self.setFixedSize(QSize(400, 300))

        buttons = [QPushButton(item, self) for item in os.listdir(self.path) if os.path.isdir(item) and not item.startswith('.')]
        buttons.insert(0, QPushButton("..", self))
        for button in buttons:
            button.clicked.connect(lambda ch, text=button.text(): self.redraw(text))
            self.layout.addWidget(button)

        silhouetteBtn = QPushButton("Run Revers Silhouette", self)
        silhouetteBtn.clicked.connect(lambda _: self.runReverseSilhouette())
        self.layout.addWidget(silhouetteBtn)
        checkBtn = QPushButton("Run Checker", self)
        checkBtn.clicked.connect(lambda _: self.runChecker())
        self.layout.addWidget(checkBtn)

        self.setCentralWidget(self.dirButtons)

    def redraw(self, pathChange):
        print(pathChange)

        self.layout.removeWidget(self.dirButtons)
        self.dirButtons = QWidget()
        self.layout = QVBoxLayout(self.dirButtons)

        os.chdir(pathChange)
        self.path = os.path.join(self.path, pathChange)
        self.path = os.path.normpath(self.path)

        label = QLabel(self.path)
        self.layout.addWidget(label)

        buttons = [QPushButton(item, self) for item in os.listdir(self.path) if os.path.isdir(item) and not item.startswith('.')]
        buttons.insert(0, QPushButton("..", self))
        for button in buttons:
            button.clicked.connect(lambda ch, text=button.text(): self.redraw(text))
            self.layout.addWidget(button)

        silhouetteBtn = QPushButton("Run Revers Silhouette", self)
        silhouetteBtn.clicked.connect(lambda _: self.runReverseSilhouette())
        self.layout.addWidget(silhouetteBtn)
        checkBtn = QPushButton("Run Checker", self)
        checkBtn.clicked.connect(lambda _: self.runChecker())
        self.layout.addWidget(checkBtn)

        self.setCentralWidget(self.dirButtons)

    def runReverseSilhouette(self):
        sil = SilhouetteMaker()
        sil.iterate_over_folders(self.path, os.path.join(self.path, "_reverse_silhouette"))

    def runChecker(self):
        sil = SilhouetteMaker()
        print(sil.check_directory(self.path))

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()