import pandas as pd
import numpy as np

from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QFrame, QPushButton, QTableWidget, QTableWidgetItem, QRadioButton
import plotly.graph_objects as go
from PyQt5.QtWebEngineWidgets import QWebEngineView

from network.tr_program import Tr_Program
from q_params import Q_Params

class Box4(QFrame):
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
        label = QLabel('BOX 4')
        vbox1.addWidget(label)

        self.table = QTableWidget(3, 4)
        vbox1.addWidget(self.table)

        vbox.addLayout(vbox1)

    def update_tr_live_30s(self):
        pass

#     def update_table(self):
#         self.dfs = self.tr_program.fetch()
#         # Wait for the event to be set
#         self.tr_program.event.wait()
#
#         self.table.clear()
#         print('self. dfs', self.dfs)
#         self.dfs = self.dfs.drop(columns=['offervalue', 'stksvalue', 'svolume', 'offervolume', 'stksvolume', 'sgta'])
#
#         # Set the table size to match the DataFrame size
#         num_rows, num_cols = self.dfs.shape
#         self.table.setRowCount(num_rows)
#         self.table.setColumnCount(num_cols)
#
#         # Set the column headers to match the DataFrame column indices
#         self.table.setHorizontalHeaderLabels(list(self.dfs.columns))
#
#         for row in range(num_rows):
#             for col in range(num_cols):
#                 item = QTableWidgetItem(str(self.dfs.iloc[row][col]))
#                 self.table.setItem(row, col, item)
#
#         self.table.resizeColumnsToContents()
#         self.table.resizeRowsToContents()
#
#         self.update_chart(self.dfs)
#
#     def update_chart(self, dfs):
#         # x = dfs['svalue']
#         # y = dfs['diff']
#         # bubble_text = dfs['hname']
#         #
#         # x = pd.to_numeric(x)
#         # y = pd.to_numeric(y)
#
#         x = dfs['hname']
#
#         y = dfs['svalue']
#         y_diff = dfs['diff']
#
#         y = pd.to_numeric(y)
#         y_diff = pd.to_numeric(y_diff)
#         y_diff = np.int64(y_diff)
#
#         def get_text_color(y_value):
#             return 'pink' if y_value > 0 else 'cornflowerblue'
#
#         fig = go.Figure(
#             data=[
#                 go.Bar(x=x, y=y, name='val_tick', marker=dict(color='grey')),
#                 go.Bar(x=x, y=y_diff, name='diff', yaxis='y2', marker=dict(color=[get_text_color(i) for i in y_diff])),
#                 #
#             ],
#
#             layout={
#                 'margin': {'l': 10, 'r': 10, 't': 30, 'b': 10},  # Minimized margins
#                 'xaxis': {'showspikes': False, },
#                 'yaxis': {'showspikes': False, },
#                 'yaxis2': {'showspikes': False, 'overlaying': 'y', 'side': 'right', },
#             }
#         )
#
#         # Convert the Plotly chart to HTML
#         raw_html = '<html><head><meta charset="utf-8" /></head><body style="margin:0; padding:0;>'
#         content = fig.to_html(full_html=False, include_plotlyjs='cdn')
#         raw_html += content.replace("window.PlotlyConfig = {MathJaxConfig: 'local'};", "")
#         raw_html += '</body></html>'
#
#         # Set up the QWebEngineView
#         self.view.setHtml(raw_html)
#         self.hbox3.addWidget(self.view)
#

