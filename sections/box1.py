from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLineEdit, \
    QLabel, QFrame, QPushButton, QRadioButton, \
    QTableWidget, QTableWidgetItem, QWidget, QComboBox

from PyQt5.QtWebEngineWidgets import QWebEngineView
from q_params import Q_Params
import csv

class Box1(QFrame):

    def __init__(self, model):
        super().__init__()

        self.p_instance = Q_Params()
        # self.controller = controller
        self.model = model
        self.dfs = None
        self.view = QWebEngineView()

        vbox = QVBoxLayout(self)
        vbox1 = QVBoxLayout()
        label = QLabel('BOX-1 Future')
        vbox1.addWidget(label)

        vbox.addLayout(vbox1)

        # self.radio_btn1 = QRadioButton("P")
        # self.radio_btn2 = QRadioButton("Q")
        # self.radio_btn1.setChecked(True)
        #
        # self.radio_btn1.toggled.connect(self.on_radio_button_toggled)
        # self.radio_btn2.toggled.connect(self.on_radio_button_toggled)
        #
        # vbox1.addWidget(self.radio_btn1)
        # vbox1.addWidget(self.radio_btn2)
        # vbox.addLayout(vbox1)
        #
        # # vbox2 = QVBoxLayout()
        # # self.radio_btn3 = QRadioButton("1st")
        # # self.radio_btn4 = QRadioButton("nxt")
        # # self.radio_btn3.setChecked(True)
        # #
        # # self.radio_btn3.toggled.connect(self.on_radio_button_toggled)
        # # self.radio_btn4.toggled.connect(self.on_radio_button_toggled)
        # #
        # # vbox2.addWidget(self.radio_btn3)
        # # vbox2.addWidget(self.radio_btn4)
        #
        # # vbox.addLayout(vbox2)
        sh = self.p_instance.shcode
        self.label = QLabel('focode: '+ str(sh))
        self.line_edit = QLineEdit()
        self.line_edit .setFixedWidth(50)
        self.line_edit.textChanged.connect(self.on_text_changed)

        # # button = QPushButton('Update')
        # # button.clicked.connect(self.on_button_clicked)
        # # button.setFixedWidth(50)

        vbox2 = QHBoxLayout()
        vbox2.addWidget(self.label)
        vbox2.addWidget(self.line_edit)
        # # vbox2.addWidget(button)

        vbox.addLayout(vbox2)

        self.combo_box = QComboBox()
        self.load_data_from_csv()

        self.combo_box.activated[str].connect(self.on_combobox_activated)
        vbox3 = QVBoxLayout()
        vbox3.addWidget(self.combo_box)

        vbox.addLayout(vbox3)

        self.table = QTableWidget(1, 1)
        vbox.addWidget(self.table)

    def load_data_from_csv(self):
        try:
            with open('f3.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    display_text = row['name']
                    code = row['code']
                    self.combo_box.addItem(f"{display_text} ({code})", code)
        except FileNotFoundError:
            print("CSV file not found.")

    def on_combobox_activated(self, text):
        # Update the label when an item is selected in the combo box
        code = text[-10:].strip('()')
        self.p_instance.set_focode(code)

    def update_tr_future(self):
        self.dfs = self.model.get_tr_future()

        self.table.clear()

        self.dfs = self.dfs.rename(columns={'stimeqrt': '거래량전일동시간',
                                            'mgjv': '미결제',
                                            'mgjvdiff': '미결제증감',
                                            'recprice': '기준가',
                                            'theoryprice': '이론가',
                                            'glyl': '괴리율',
                                            'lastmonth':'만기일',
                                            'jandatecnt':'잔여일',

                                            'gmprice':'근월물 현재가',
                                            'gmchange':'근월물 전일대비',
                                            'gmdiff': '근월물 등락율',

                                            'impv': '내재변동성',
                                            'sbasis' :'시장 베이시스',
                                            'ibasis' : '이론 베이시스',
                                            'gmfutcode': '근월물 코드',
                                            })

        self.dfs = self.dfs.drop(columns=['sign',
                                          'value',
                                          'uplmtprice',
                                          'dnlmtprice',
                                          'high52w',
                                          'low52w',
                                          ])
        # # Set the table size to match the DataFrame size
        num_rows, num_cols = self.dfs.shape
        self.table.setRowCount(num_cols)
        self.table.setColumnCount(num_rows)

        self.table.setVerticalHeaderLabels(list(self.dfs.columns))

        # 1 and 10
        for row in range(num_rows):
            for col in range(num_cols):
                val = self.dfs.iloc[row][col]
                item = QTableWidgetItem(str(val))
                self.table.setItem(col, row, item)

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def on_radio_button_toggled(self):
        if self.radio_btn1.isChecked():
            self.p_instance.set_market('p')
        elif self.radio_btn2.isChecked():
            self.p_instance.set_market('q')

    def on_text_changed(self, text):
        print('text future ---', text )
        self.label.setText('Future-' + text)
        self.p_instance.set_focode(text)

    # def refresh(self):
    #     print('q')
