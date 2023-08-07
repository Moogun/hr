from PyQt5.QtWidgets import QVBoxLayout, QLabel, QFrame

class UpperRight(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("border: 1px solid gray;")
        layout = QVBoxLayout(self)
        label = QLabel('Upper Right')
        layout.addWidget(label)