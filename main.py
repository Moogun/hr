import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QFrame, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QTimer, QDate, QTime,Qt
from PyQt5.QtGui import QColor

import leftPane
import rightTopPane
from clickEvent import button_login_clicked, button_mk_cap_clicked, button_tr_vol_clicked, button_tr_val_clicked

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 Example')
        self.setGeometry(400, 100, 400, 200)

        # Create a central widget and set the layout for it
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        # Create a top-level layout for the main window
        main_layout = QHBoxLayout(central_widget)

        # Create the left pane using the leftPane.py module
        button_login, button_mk_cap, button_tr_vol, button_tr_val, left_widget = leftPane.setup()
        main_layout.addWidget(left_widget)

        # Create the right pane using the leftPane.py module
        right_label, right_label2, right_widget = rightTopPane.setup()
        main_layout.addWidget(right_widget)

        left_widget.setStyleSheet("border: 0.5px solid darkGray; max-width: 200px;")
        right_widget.setStyleSheet("border: 0.5px solid darkGray;")

        self.setLayout(main_layout)

        # Connect button clicks to their corresponding functions from clickEvent.py
        button_login.clicked.connect(lambda: button_login_clicked(right_label))
        button_mk_cap.clicked.connect(lambda: button_mk_cap_clicked(right_label, right_label2))
        button_tr_vol.clicked.connect(lambda: (button_tr_vol_clicked(right_label), self.remove_last_label()))
        button_tr_val.clicked.connect(lambda: (button_tr_vol_clicked(right_label), self.add_label()))

        # Create and start the timer to update the time label every second
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.update_time_label)

        # List to keep track of the added labels
        self.labels = []

    def update_time_label(self):
        now = QDate.currentDate()
        time = QTime.currentTime()
        self.setWindowTitle(now.toString(Qt.ISODate) + " " + time.toString('hh.mm.ss'))  # Initial update of the time label

    def add_label(self):
        # Create a new label and add it to the layout
        label = QLabel('New Label', self)
        self.labels.append(label)
        print('--', len(self.labels))
        # self.right_widget().layout().addWidget(label)
        self.centralWidget().layout().addWidget(label)

    def remove_last_label(self):
        if self.labels:
            # Get the last added label and remove it from the layout and the list
            label = self.labels.pop()
            label.deleteLater()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Create and show the main window
    window = App()
    window.show()
    # Start the application event loop
    sys.exit(app.exec_())
