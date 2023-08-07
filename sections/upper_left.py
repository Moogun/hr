from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, \
    QLabel, QFrame, QPushButton,  \
    QTableWidget, QTableWidgetItem
import random

class UpperLeft(QFrame):

    def __init__(self):
        super().__init__()

        # # Create the main vertical layout
        # vbox = QVBoxLayout(self)
        #
        # # Create the first horizontal layout for the label and button
        # hbox1 = QHBoxLayout()
        # # label = QLabel('Cap')
        # # button = QPushButton('Update')
        # # hbox1.addWidget(label)
        # # hbox1.addWidget(button)
        #
        # # Generate 3x4 random data
        # random_data = [[random.random() for _ in range(4)] for _ in range(3)]
        #
        # hbox2 = QHBoxLayout()
        # hbox3 = QHBoxLayout()
        #
        #
        # # Add the horizontal layouts to the main vertical layout
        # vbox.addLayout(hbox1)
        # vbox.addLayout(hbox2)
        # vbox.addLayout(hbox3)

        self.setStyleSheet("border: 1px solid gray;")
        layout = QVBoxLayout(self)
        label = QLabel('Upper left')
        layout.addWidget(label)