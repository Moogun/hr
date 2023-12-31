import pandas as pd
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QFrame, QPushButton, QTableWidget, QTableWidgetItem, QRadioButton
from color_book import color_dict
import plotly.graph_objects as go
from PyQt5.QtWebEngineWidgets import QWebEngineView
from q_params import Q_Params
from PyQt5.QtGui import QColor, QBrush

class Box7(QFrame):
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
        label = QLabel('BOX-7 TODAY')
        vbox1.addWidget(label)

        self.table = QTableWidget(3, 4)
        vbox1.addWidget(self.table)

        vbox.addLayout(vbox1)

        self.hbox1 = QHBoxLayout()
        self.view = QWebEngineView()
        vbox.addLayout(self.hbox1)

    def update_tr_today(self):
        self.dfs = self.model.get_tr_today()
        print('get_tr_today', self.dfs)

        self.table.clear()

        # self.dfs = self.dfs.rename(columns={'tjj0000_vol': '사모',
        #                                    'tjj0001_vol': '증권',
        #                                    'tjj0002_vol': '보험',
        #                                    })
        #
        # field = ['volume',
        #          '기관', '외인계', '기타계(기타+국가)' ]
        #
        # for i in field:
        #     self.dfs[i] = (pd.to_numeric(self.dfs[i]) / 100000).round(3)
        #
        self.dfs = self.dfs.drop(columns=['sign',
                                          'change',
                                          'recprice', 'avg',
                                          'uplmtprice','dnlmtprice',
                                          'opentime',
                                          'memedan',
                                          'offernocd1', 'bidnocd1',
                                          'offernocd2', 'bidnocd2',
                                          'listing',
                                          'memedan',
                                          'offernocd1','bidno1',
                                          'offernocd2','bidno2',
                                          'offernocd3','bidno3',
                                          'offernocd4','bidno4',
                                          'offernocd5','bidno5',
                                          'offernocd5',
                                          # 'janginfo',
                                          # # 'tongwha',
                                          # 'shcode', 'target','capital',
                                          # 'gsmm', 'listdate',
                                          # 'spac_gubun',
                                          # 'issueprice',
                                          #
                                          # 'shterm_text',
                                          # 'svi_uplmtprice',
                                          # 'svi_dnlmtprice',
                                          # 'low_lqdt_gu',
                                          # 'ty_text',
                                          # 'info1',
                                          # 'info2',
                                          # 'info3',
                                          # 'info4',
                                          #
                                          # 'ftrad',
                                          ])

        # # Set the table size to match the DataFrame size
        num_rows, num_cols = self.dfs.shape
        # self.table.setRowCount(num_rows)
        # self.table.setColumnCount(num_cols)
        self.table.setRowCount(num_cols)
        self.table.setColumnCount(num_rows)

        # Set the column headers to match the DataFrame column indices
        # self.table.setHorizontalHeaderLabels(list(self.dfs.columns))
        self.table.setVerticalHeaderLabels(list(self.dfs.columns))

        # 1 and 10
        for row in range(num_rows):
            for col in range(num_cols):

                val = self.dfs.iloc[row][col]
                item = QTableWidgetItem(str(val))
                self.table.setItem(col, row, item)

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
