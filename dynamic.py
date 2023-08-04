import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget

class DynamicObjectApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Dynamic Object Example')
        self.setGeometry(100, 100, 400, 300)

        # Create a central widget and a vertical layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create a button to add an object dynamically
        self.add_button = QPushButton('Add Object', self)
        self.add_button.clicked.connect(self.add_object)
        layout.addWidget(self.add_button)

        # Create a button to remove the last added object dynamically
        self.remove_button = QPushButton('Remove Last Object', self)
        self.remove_button.clicked.connect(self.remove_object)
        layout.addWidget(self.remove_button)

        # List to keep track of the added objects
        self.objects = []

    def add_object(self):
        # For this example, let's add a QLabel, but you can add any PyQt5 widget here
        new_object = QLabel('New Object', self)
        self.objects.append(new_object)
        self.centralWidget().layout().addWidget(new_object)

    def remove_object(self):
        if self.objects:
            # Get the last added object and remove it from the layout and the list
            obj = self.objects.pop()
            obj.deleteLater()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DynamicObjectApp()
    window.show()
    sys.exit(app.exec_())
