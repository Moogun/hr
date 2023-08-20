import pandas as pd
import numpy as np

from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QFrame, QPushButton, QTableWidget, QTableWidgetItem, QRadioButton
import plotly.graph_objects as go
from PyQt5.QtWebEngineWidgets import QWebEngineView

from q_params import Q_Params
from color_book import color_dict

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

        self.hbox3 = QHBoxLayout()
        self.view = QWebEngineView()
        vbox.addLayout(self.hbox3)

    def update_tr_half_min(self):
        self.dfs = self.model.get_tr_half_min()
        print('get_tr_half_min ', self.dfs)

        self.table.clear()
        print('self. dfs', self.dfs)
        self.dfs = self.dfs.drop(columns=['sign', 'open', 'high', 'low',
                                          'totofferrem', 'totbidrem', 'mdvolumetm', 'msvolumetm',
                                          'volume', 'mdchecnttm', 'mschecnttm', 'mdvolume', 'msvolume'
                                          ])

         # Set the table size to match the DataFrame size
        num_rows, num_cols = self.dfs.shape
        self.table.setRowCount(num_rows)
        self.table.setColumnCount(num_cols)

        # Set the column headers to match the DataFrame column indices
        self.table.setHorizontalHeaderLabels(list(self.dfs.columns))

        for row in range(num_rows):
            for col in range(num_cols):
                item = QTableWidgetItem(str(self.dfs.iloc[row][col]))
                self.table.setItem(row, col, item)

        # self.color_rows(num_rows, num_cols)

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

        self.update_chart(self.dfs)
#     def color_rows(self, num_rows, num_cols):
#         for row in range(num_rows):
#             prev_row = row-1
#             if row > 1:
#                 cell_value = pd.to_numeric(self.dfs.loc[row, 'revolume'])
#                 prev_cell_value = pd.to_numeric(self.dfs.loc[prev_row, 'revolume'])
#
#                 print('cell_value', cell_value)
#                 print('prev_', prev_cell_value)
#
#                 if cell_value > prev_cell_value:
#                     print('posi')
#                     self.color_row(row, color_dict['pink'])
#                 else:
#                     print('nega')
#                     self.color_row(row, color_dict['gray'])

    def color_row(self, row, color):
        row_items = [self.table.item(row, col) for col in range(self.table.columnCount())]
        for item in row_items:
            item.setBackground(color)

    def update_chart(self, dfs):
        x = dfs['chetime']
        y = dfs['cvolume']
        # bubble_text = dfs['hname']
        #
        # x = pd.to_numeric(x)
        # y = pd.to_numeric(y)

        # x = dfs['hname']
        #
        # y = dfs['svalue']
        y_diff = dfs['diff']

        x = pd.to_numeric(x)
        y = pd.to_numeric(y)
        y_diff = pd.to_numeric(y_diff)
        y_diff = np.int64(y_diff)

        # def get_text_color(y_value):
        #     return 'pink' if y_value > 0 else 'cornflowerblue'

        fig = go.Figure(
            data=[
                go.Bar(x=x, y=y,  name='vol', marker=dict(color='grey')),
                go.Scatter(x=x, y=y_diff,  yaxis='y2', mode = 'lines+markers', marker=dict(color='red')),
                # go.Bar(x=x, y=y_diff, name='diff', yaxis='y2', marker=dict(color=[get_text_color(i) for i in y_diff])),
                #
            ],

            layout={
                'margin': {'l': 10, 'r': 10, 't': 30, 'b': 10},  # Minimized margins
                'xaxis': {'showspikes': False, },
                'yaxis': {'showspikes': False, },
                'yaxis2': {'showspikes': False, 'overlaying': 'y', 'side': 'right', },
            }
        )

        # Convert the Plotly chart to HTML
        raw_html = '<html><head><meta charset="utf-8" /></head><body style="margin:0; padding:0;>'
        content = fig.to_html(full_html=False, include_plotlyjs='cdn')
        raw_html += content.replace("window.PlotlyConfig = {MathJaxConfig: 'local'};", "")
        raw_html += '</body></html>'

        # Set up the QWebEngineView
        self.view.setHtml(raw_html)
        self.hbox3.addWidget(self.view)


