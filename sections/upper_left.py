from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, \
    QLabel, QFrame, QPushButton, QRadioButton, \
    QTableWidget, QTableWidgetItem
import random

class UpperLeft(QFrame):

    def __init__(self):
        super().__init__()

        # Create the main vertical layout
        vbox = QVBoxLayout(self)

        # Create the first horizontal layout for the label and button
        # hbox1 = QHBoxLayout()
        vbox1 = QVBoxLayout()

        self.radio_btn1 = QRadioButton("P")
        self.radio_btn2 = QRadioButton("Q")
        self.radio_btn1.setChecked(True)

        self.radio_btn1.toggled.connect(self.on_radio_button_toggled)
        self.radio_btn2.toggled.connect(self.on_radio_button_toggled)

        vbox1.addWidget(self.radio_btn1)
        vbox1.addWidget(self.radio_btn2)

        vbox2 = QVBoxLayout()
        self.radio_btn3 = QRadioButton("1st")
        self.radio_btn4 = QRadioButton("nxt")
        self.radio_btn3.setChecked(True)

        self.radio_btn3.toggled.connect(self.on_radio_button_toggled)
        self.radio_btn4.toggled.connect(self.on_radio_button_toggled)

        vbox2.addWidget(self.radio_btn3)
        vbox2.addWidget(self.radio_btn4)

        # self.dfs = None
        # self.table = QTableWidget(3, 4)
        # hbox2 = QHBoxLayout()
        # hbox2.addWidget(self.table)
        #
        # # Create hbox3 for the chart
        # self.hbox3 = QHBoxLayout()
        # self.view = QWebEngineView()
        #
        # # Add the horizontal layouts to the main vertical layout
        vbox.addLayout(vbox1)
        vbox.addLayout(vbox2)
        # vbox.addLayout(self.hbox3)

    def on_radio_button_toggled(self):
        # Update the label text when a radio button is toggled
        if self.radio_btn1.isChecked():
            print('1')
            # self.tr_val.set_gubun('1')
        elif self.radio_btn2.isChecked():
            print('2')
            # self.tr_val.set_gubun('2')

    def refresh(self):
        print('q')