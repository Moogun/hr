from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QPushButton
from PyQt5.QtCore import Qt

def setup():

    # Create the right pane label
    right_label = QLabel('None Selected')
    right_label2 = QLabel('label2')

    # Create a vertical layout for the right pane
    right_layout = QVBoxLayout()
    right_layout.addWidget(right_label)
    right_layout.addWidget(right_label2)
    right_layout.addStretch()  # To push the label to the top

    # Create a widget for the right pane and set its layout
    right_widget = QWidget()
    right_widget.setLayout(right_layout)

    return right_label, right_label2, right_widget
