from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QPushButton
from PyQt5.QtCore import QTimer, QDate, QTime,Qt

def setup():

    # Create buttons for the left pane
    button_login = QPushButton('Login')
    button_mk_cap = QPushButton('Market Cap')
    button_tr_vol = QPushButton('Trading Vol')
    button_tr_val = QPushButton('Trading Value')

    # Create a horizontal layout for the left pane
    left_layout = QVBoxLayout()
    left_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

    # Add buttons to the left layout
    # left_layout.addWidget(clock_label)
    left_layout.addWidget(button_login)
    left_layout.addWidget(button_mk_cap)
    left_layout.addWidget(button_tr_vol)
    left_layout.addWidget(button_tr_val)

    # Create a widget for the left pane and set its layout
    left_widget = QWidget()
    left_widget.setLayout(left_layout)

    return button_login, button_mk_cap, button_tr_vol, button_tr_val, left_widget
