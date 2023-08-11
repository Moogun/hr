from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, \
    QLabel, QFrame, QPushButton,  \
    QTableWidget, QTableWidgetItem
import random

class UpperLeft(QFrame):

    def __init__(self):
        super().__init__()

        self.setStyleSheet("border: 1px solid gray;")
        layout = QVBoxLayout(self)
        label = QLabel('Upper left')
        layout.addWidget(label)

    def refresh(self):
        print('q')