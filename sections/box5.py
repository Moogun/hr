from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, \
    QLabel, QFrame, QPushButton, QRadioButton, QTableWidget, QTableWidgetItem

class Box5(QFrame):
    def __init__(self, model):
        super().__init__()
        self.model = model

        vbox = QVBoxLayout(self)

        vbox1 = QVBoxLayout()
        label = QLabel('Box 5')
        vbox1.addWidget(label)

        self.table = QTableWidget(3, 4)
        vbox1.addWidget(self.table)

        vbox.addLayout(vbox1)