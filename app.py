
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFrame, QMessageBox
from PyQt5.QtCore import Qt

from sections.upper_left import UpperLeft
from sections.upper_middle import UpperMiddle
from sections.upper_right import UpperRight
from sections.upper_right2 import UpperRight2

from sections.lower_left import LowerLeft
from sections.lower_middle import LowerMiddle
from sections.lower_right import LowerRight
from sections.lower_right2 import LowerRight2

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

        self.ul = UpperLeft()
        upper_hbox.addWidget(self.ul)
        self.um = UpperMiddle()
        upper_hbox.addWidget(self.um)
        self.ur = UpperRight()
        upper_hbox.addWidget(self.ur)
        self.ur2 = UpperRight2()
        upper_hbox.addWidget(self.ur2)
        vbox.addLayout(upper_hbox)

        # Create and style lower row
        lower_hbox = QHBoxLayout()

        self.ll = LowerLeft()
        lower_hbox.addWidget(self.ll)
        self.lm = LowerMiddle()
        lower_hbox.addWidget(self.lm)
        self.lr = LowerRight()
        lower_hbox.addWidget(self.lr)
        self.lr2 = LowerRight2()
        lower_hbox.addWidget(self.lr2)

        vbox.addLayout(lower_hbox)

        self.setLayout(vbox)

        self.setWindowTitle('Six Sections')
        self.setGeometry(300, 300, 600, 400)
        self.show()

        #Login
        login = Login('Taketheg', 'bwii1145', 'Bwiisi07@3')
        login.login()

    def keyPressEvent(self, event):
        key = event.key()
        match key:
            case Qt.Key_Q:
                self.ul.refresh()
            case Qt.Key_W:
                self.um.refresh()
            case Qt.Key_E:
                self.ur.refresh()
            case Qt.Key_R:
                self.ur2.refresh()

            case Qt.Key_A:
                self.ll.refresh()
            case Qt.Key_S:
                self.lm.refresh()
            case Qt.Key_D:
                self.lr.refresh()
            case Qt.Key_F:
                self.lr2.refresh()
            case _:
                print('No match')


    # def change_color_layout1(self):
    #     self.set_widget_bg_color(self.layout1_widget, "blue")