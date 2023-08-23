import pandas as pd
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QFrame, QPushButton, QTableWidget, QTableWidgetItem, QRadioButton

import plotly.graph_objects as go
from PyQt5.QtWebEngineWidgets import QWebEngineView
from color_book import color_dict
from q_params import Q_Params

class Box8(QFrame):
    def __init__(self, model):
        super().__init__()
        self.p_instance = Q_Params()
        self.model = model
        self.dfs = None
        self.view = QWebEngineView()

        vbox = QVBoxLayout(self)

        vbox1 = QVBoxLayout()
        label = QLabel('BOX-8 READY_SHORT')
        vbox1.addWidget(label)

        self.table = QTableWidget(1, 1)
        vbox1.addWidget(self.table)

        vbox.addLayout(vbox1)

        self.hbox1 = QHBoxLayout()
        self.view = QWebEngineView()
        vbox.addLayout(self.hbox1)


    def update_ready_short(self):
        self.dfs = self.model.get_ready_short()
        print('view update_get_ready_short', self.dfs)

        self.table.clear()

        if self.dfs.empty:
            print("empty data")
        else:
            self.dfs = self.dfs.drop(columns=['sign', 'volume', 'tovalue', 'shcode'])

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

            self.color_rows(num_rows, num_cols)
            self.table.resizeColumnsToContents()
            self.table.resizeRowsToContents()

            self.update_chart(self.dfs)

    def color_rows(self, num_rows, num_cols):
        for row in range(num_rows):

            diff = pd.to_numeric(self.dfs.loc[row, 'tovoldif'])
            if diff < 0:
                self.color_row(row, color_dict['cornflowerblue'])
            else:
                self.color_row(row, color_dict['pink'])


    def color_row(self, row, color):
        row_items = [self.table.item(row, col) for col in range(self.table.columnCount())]
        for item in row_items:
            item.setBackground(color)

    def update_chart(self, dfs):
        x = dfs['date']
        y = dfs['price']
        y = pd.to_numeric(y)

        y_bar = dfs['tovolume']
        y_bar = pd.to_numeric(y_bar)

        y_bar2 = dfs['upvolume']
        y_bar2 = pd.to_numeric(y_bar2)

        y_bar3 = dfs['dnvolume']
        y_bar3 = pd.to_numeric(y_bar3)

        fig = go.Figure(
            data=[
                go.Scatter(y=y, x=x, name='price', mode='lines+markers'),
                go.Scatter(x=x, y=y_bar, mode='lines+markers', yaxis='y2', name='remaining',
                           marker=dict(color='gray')),
                # go.Bar(x=x, y=y_bar2, name='new', marker=dict(color='lightblue')),
                # go.Bar(x=x, y=y_bar3, name='off', marker=dict(color='salmon')),
            ],
            layout={
                'margin': {'l': 10, 'r': 10, 't': 30, 'b': 10},  # Minimized margins
                'xaxis': {'showspikes': False, 'autorange': 'reversed'},  # Remove x-axis borders
                'yaxis': {'showspikes': False},
                'yaxis2': {'showspikes': False, 'overlaying': 'y', 'side': 'right'},
                # Second y-axis# Remove y-axis borders
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
