from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLineEdit, \
    QLabel, QFrame, QPushButton, QRadioButton, \
    QTableWidget, QTableWidgetItem, QWidget

from q_params import Q_Params

class Box1(QFrame):

    def __init__(self, controller):
        super().__init__()

        self.p_instance = Q_Params()
        self.controller = controller

        vbox = QVBoxLayout(self)
        vbox1 = QVBoxLayout()

        self.radio_btn1 = QRadioButton("P")
        self.radio_btn2 = QRadioButton("Q")
        self.radio_btn1.setChecked(True)

        self.radio_btn1.toggled.connect(self.on_radio_button_toggled)
        self.radio_btn2.toggled.connect(self.on_radio_button_toggled)

        vbox1.addWidget(self.radio_btn1)
        vbox1.addWidget(self.radio_btn2)
        vbox.addLayout(vbox1)

        # vbox2 = QVBoxLayout()
        # self.radio_btn3 = QRadioButton("1st")
        # self.radio_btn4 = QRadioButton("nxt")
        # self.radio_btn3.setChecked(True)
        #
        # self.radio_btn3.toggled.connect(self.on_radio_button_toggled)
        # self.radio_btn4.toggled.connect(self.on_radio_button_toggled)
        #
        # vbox2.addWidget(self.radio_btn3)
        # vbox2.addWidget(self.radio_btn4)

        # vbox.addLayout(vbox2)

        self.label = QLabel('SH')
        self.line_edit = QLineEdit()
        self.line_edit .setFixedWidth(50)
        self.line_edit.textChanged.connect(self.on_text_changed)

        # button = QPushButton('Update')
        # button.clicked.connect(self.on_button_clicked)
        # button.setFixedWidth(50)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.label)
        vbox2.addWidget(self.line_edit)
        # vbox2.addWidget(button)
        vbox.addLayout(vbox2)

    def on_radio_button_toggled(self):
        if self.radio_btn1.isChecked():
            self.p_instance.set_market('p')
        elif self.radio_btn2.isChecked():
            self.p_instance.set_market('q')

    def on_text_changed(self, text):
        self.label.setText('SH-'+ text)
        if len(text) == 6:
            self.p_instance.set_shcode(text)
            print('shcode updated', self.p_instance.shcode)
        else:
            print('not 6 digits')

    def refresh(self):
        print('q')