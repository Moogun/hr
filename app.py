
from PyQt5.QtWidgets import QMainWindow
from network.login import Login

from model import Model
from network_model import NetworkModel
from controller import Controller
from view import View

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        print('app')
        self.model = Model()
        self.network_model = NetworkModel()
        self.controller = Controller(self.model, self.network_model)
        self.view = View(self.model, self.controller)
        self.controller.set_view(self.view)

        self.setCentralWidget(self.view)
        self.setWindowTitle('MVC Example')


        #Login
        login = Login('Taketheg', 'bwii1145', 'Bwiisi07@3')
        login.login()


    # def change_color_layout1(self):
    #     self.set_widget_bg_color(self.layout1_widget, "blue")