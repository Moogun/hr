import pandas as pd
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QFrame, QPushButton, QTableWidget, QTableWidgetItem, QRadioButton
from color_book import color_dict
import plotly.graph_objects as go
from PyQt5.QtWebEngineWidgets import QWebEngineView
from q_params import Q_Params
from PyQt5.QtGui import QColor, QBrush
from PyQt5.QtCore import Qt

class Box2(QFrame):
    def __init__(self, model):
        super().__init__()
        self.p_instance = Q_Params()
        self.model = model
        self.dfs = None
        self.view = QWebEngineView()

        # 현재가 분차트, 대량 체결량
        # 프로그램매매
        # 거래원
        # 대차거래, 공매도

        vbox = QVBoxLayout(self)

        vbox1 = QVBoxLayout()
        label = QLabel('BOX-2 DAYS-VOL 10만')
        vbox1.addWidget(label)

        self.table = QTableWidget(3, 4)
        vbox1.addWidget(self.table)

        vbox.addLayout(vbox1)

        self.hbox1 = QHBoxLayout()
        self.view = QWebEngineView()
        vbox.addLayout(self.hbox1)

    def update_tr_days(self):
        self.dfs = self.model.get_tr_days()
        print('get_tr_days ', self.dfs)

        self.table.clear()

        self.dfs = self.dfs.rename(columns={'tjj0000_vol': '사모',
                                           'tjj0001_vol': '증권',
                                           'tjj0002_vol': '보험',
                                           'tjj0003_vol': '투신',
                                           'tjj0004_vol': '은행',
                                           'tjj0005_vol': '종금',
                                           'tjj0006_vol': '기금',
                                           'tjj0007_vol': '기타',
                                           'tjj0008_vol': '개인',
                                           'tjj0009_vol': '등록외국',
                                           'tjj0010_vol': '미등록외국',
                                           'tjj0011_vol': '국가외',
                                           'tjj0018_vol': '기관',
                                           'tjj0016_vol': '외인계',
                                           'tjj0017_vol': '기타계(기타+국가)',
                                           'tjj0000_dan': '사모(단가)',
                                           'tjj0001_dan': '증권(단가)',
                                           'tjj0002_dan': '보험(단가)',
                                           'tjj0003_dan': '투신(단가)',
                                           'tjj0004_dan': '은행(단가)',
                                           'tjj0005_dan': '종금(단가)',
                                           'tjj0006_dan': '기금(단가)',
                                           'tjj0007_dan': '기타(단가)',
                                           'tjj0008_dan': '개인(단가)',
                                           'tjj0009_dan': '등록외국(단가)',
                                           'tjj0010_dan': '미등록외국(단가)',
                                           'tjj0011_dan': '국가외(단가)',
                                           'tjj0018_dan': '기관(단가)',
                                           'tjj0016_dan': '외인계(단가)',
                                           'tjj0017_dan': '기타계(기타+국가)(단가)',
                                           })

        field = ['volume',
                '사모', '증권',
                 # '보험',
                 '투신',
                 # '은행', '종금',
                 '기금',
                 # '기타',
                 '개인',
                 # '등록외국',
                 # '미등록외국', '국가외',
                 '기관', '외인계', '기타계(기타+국가)' ]

        for i in field:
            self.dfs[i] = (pd.to_numeric(self.dfs[i]) / 100000).round(1)

        self.dfs = self.dfs.drop(columns=['sign','diff',
                                          'volume',
                                          '은행', '종금', '미등록외국','등록외국',
                                          '국가외','기타계(기타+국가)',
                                          '기타',
                                          '보험',
                                          '사모(단가)', '증권(단가)', '보험(단가)', '투신(단가)','기금(단가)',
                                          '기타(단가)', '개인(단가)', '등록외국(단가)', '기관(단가)','외인계(단가)',
                                          '은행(단가)', '종금(단가)', '미등록외국(단가)', '국가외(단가)','기타계(기타+국가)(단가)'
                                          ])

        # Set the table size to match the DataFrame size
        num_rows, num_cols = self.dfs.shape
        self.table.setRowCount(num_rows)
        self.table.setColumnCount(num_cols)

        # Set the column headers to match the DataFrame column indices
        self.table.setHorizontalHeaderLabels(list(self.dfs.columns))

        for row in range(num_rows):
            for col in range(num_cols):

                val = self.dfs.iloc[row][col]
                if val == 0:
                    val = '-'
                item = QTableWidgetItem(str(val))
                self.table.setItem(row, col, item)
                # print('val', val, type(val))

                try:
                    val = pd.to_numeric(val)
                    if  val <= -3:
                        item.setForeground(QBrush(Qt.blue))
                        item.setBackground(color_dict['gray3'])
                    elif 0 < val < -3:
                        item.setForeground(QBrush(Qt.blue))

                    elif 3 > val > 0:
                        item.setForeground(QBrush(Qt.darkRed))

                    elif val >= 3:
                        item.setForeground(QBrush(Qt.darkRed))
                        item.setBackground(color_dict['red1'])
                    else:
                        print('none')

                except (ValueError, TypeError):
                    print('ValueError', ValueError)


        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
