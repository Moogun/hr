
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame
from sections.upper_left import UpperLeft
from sections.upper_middle import UpperMiddle
from sections.upper_right import UpperRight

from sections.lower_left import LowerLeft
from sections.lower_middle import LowerMiddle
from sections.lower_right import LowerRight

from network.login import Login
from company import Company

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create layouts
        vbox = QVBoxLayout()

        # Create and style upper row
        upper_hbox = QHBoxLayout()
        upper_hbox.addWidget(UpperLeft())
        upper_hbox.addWidget(UpperMiddle())
        upper_hbox.addWidget(UpperRight())
        vbox.addLayout(upper_hbox)

        # Create and style lower row
        lower_hbox = QHBoxLayout()
        lower_hbox.addWidget(LowerLeft())
        lower_hbox.addWidget(LowerMiddle())
        lower_hbox.addWidget(LowerRight())

        vbox.addLayout(lower_hbox)

        self.setLayout(vbox)

        self.setWindowTitle('Six Sections')
        self.setGeometry(300, 300, 600, 400)
        self.show()

        #Login
        login = Login('Taketheg', 'bwii1145', 'Bwiisi07@3')
        login.login()

