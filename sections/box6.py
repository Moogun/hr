import pandas as pd
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QFrame, QPushButton, QTableWidget, QTableWidgetItem, QRadioButton

import plotly.graph_objects as go
from PyQt5.QtWebEngineWidgets import QWebEngineView
from color_book import color_dict
from q_params import Q_Params

class Box6(QFrame):
    def __init__(self, model):
        super().__init__()
        self.p_instance = Q_Params()
        self.model = model
        self.dfs = None
        self.view = QWebEngineView()

        vbox = QVBoxLayout(self)

        vbox1 = QVBoxLayout()
        label = QLabel('PRO SHCODE')
        vbox1.addWidget(label)

        self.table = QTableWidget(1, 1)
        vbox1.addWidget(self.table)

        vbox.addLayout(vbox1)

        self.hbox1 = QHBoxLayout()
        self.view = QWebEngineView()
        vbox.addLayout(self.hbox1)


    def update_tr_pro_shcode(self):
        self.dfs = self.model.get_tr_pro_shcode()
        print('view update_tr_pro_shcode', self.dfs)
        if self.dfs is not None:
            self.table.clear()

            # a = pd.to_numeric(self.dfs['stksvolume'])
            # b = pd.to_numeric(self.dfs['offervolume'])
            # c = pd.to_numeric(self.dfs['volume'])
            # self.dfs['sell_ratio'] = (b / c).round(2)
            # self.dfs['buy_ratio'] = (a / c).round(2)
            #
            # tril = 1000000000000
            # self.dfs['sgta'] = (pd.to_numeric(self.dfs['sgta']) / tril).round(2)
            self.dfs = self.dfs.drop(columns=['date', 'sign','offervalue', 'stksvalue',
                                              'offervolume','stksvolume',])

            num_rows, num_cols = self.dfs.shape
            self.table.setRowCount(num_rows)
            self.table.setColumnCount(num_cols)

            self.table.setHorizontalHeaderLabels(list(self.dfs.columns))

            for row in range(num_rows):
                for col in range(num_cols):
                    item = QTableWidgetItem(str(self.dfs.iloc[row][col]))
                    self.table.setItem(row, col, item)

            self.update_chart(self.dfs)
            # self.color_rows(num_rows, num_cols)

    def update_chart(self, dfs):
        print('dfs', dfs, '0000')
        x = dfs['time']
        y_price = dfs['price']

        x = pd.to_numeric(x)
        y_price = pd.to_numeric(y_price)

        y_bar = dfs['svolume']
        y_bar = pd.to_numeric(y_bar)

        miny, maxy = self.adjust_y_axis_range(y_bar)
        print('ranges', miny, maxy)

        fig = go.Figure(
            data=[
                go.Bar(x=x, y=y_bar, name='vol', marker=dict(color='gray')),
                go.Scatter(x=x, y=y_price, name='price', yaxis='y2', mode='lines+markers'),
            ],
            layout={
                'margin': {'l': 10, 'r': 10, 't': 30, 'b': 10},  # Minimized margins
                'xaxis': {'showspikes': False, },  # Remove x-axis borders
                'yaxis': {'showspikes': False, 'range': [miny, maxy]},
                'yaxis2': {'showspikes': False, 'overlaying': 'y', 'side': 'right'},  # Second y-axis# Remove y-axis borders
            }
        )

        # Convert the Plotly chart to HTML
        raw_html = '<html><head><meta charset="utf-8" /></head><body style="margin:0; padding:0;>'
        content = fig.to_html(full_html=False, include_plotlyjs='cdn')
        raw_html += content.replace("window.PlotlyConfig = {MathJaxConfig: 'local'};", "")
        raw_html += '</body></html>'

        # Set up the QWebEngineView
        self.view.setHtml(raw_html)
        self.hbox1.addWidget(self.view)

    def adjust_y_axis_range(self, y):
        print('y', y)
        min_y = min(y)
        max_y = max(y)

        y_padding = (max_y - min_y) * 0.1
        min_y -= y_padding
        max_y += y_padding

        return (min_y, max_y)