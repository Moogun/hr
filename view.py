from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

from sections.box1 import Box1
from sections.box2 import Box2
from sections.box3 import Box3
from sections.box4 import Box4
from sections.box5 import Box5

from q_params import Q_Params
class View(QWidget):
    def __init__(self, model, controller):
        super().__init__()
        self.model = model
        self.controller = controller

        self.p_instance = Q_Params()

        self.box1 = Box1(self.controller)
        self.box2 = Box2()
        self.box3 = Box3(self.model)
        self.box4 = Box4(self.model)
        self.box5 = Box5(self.model)

        vbox = QVBoxLayout()

        u_box = QHBoxLayout()
        u_box.addWidget(self.box1)
        u_box.addWidget(self.box3)
        u_box.addWidget(self.box5)

        l_box = QHBoxLayout()
        l_box.addWidget(self.box2)
        l_box.addWidget(self.box4)

        vbox.addLayout(u_box)
        vbox.addLayout(l_box)

        self.setLayout(vbox)

    def update_tr_val(self):
        self.box3.update_tr_val()
        # print(self.model.get_tr_val())
        # self.label.setText(f"Data: {self.model.get_tr_val()}")
    def update_tr_pro(self):
        self.box5.update_tr_pro()

    def update_tr_live(self):
        self.box4.update_tr_live()

    def keyPressEvent(self, event):
        key = event.key()
        match key:
            case Qt.Key_Q:
                print('111')
            case Qt.Key_3:
                # not sure if this is good or bad
                self.p_instance.market = 'p'
                self.controller.ask_tr_val()
                # self.box1.ask_tr_val()
            case Qt.Key_E:
                self.p_instance.market = 'q'
                self.controller.ask_tr_val()
                # self.box1.ask_tr_val()

            case Qt.Key_5:
                self.p_instance.market = 'p'
                self.controller.ask_tr_pro()
                # self.box1.ask_tr_pro()

            case Qt.Key_T:
                self.p_instance.market = 'q'
                self.controller.ask_tr_pro()

            case Qt.Key_4:
                print('key4 shcode', self.p_instance.shcode)

            #     self.ul.refresh()
            # case Qt.Key_W:
            #     self.um.refresh()
            # case Qt.Key_E:
            #     self.ur.refresh()
            # case Qt.Key_R:
            #     self.ur2.refresh()
            #
            # case Qt.Key_A:
            #     self.ll.refresh()
            # case Qt.Key_S:
            #     self.lm.refresh()
            # case Qt.Key_D:
            #     self.lr.refresh()
            # case Qt.Key_F:
            #     self.lr2.refresh()
            case _:
                print('No match')

    def set_shcode(self, shcode):
        self.p_instance.shcode = shcode

