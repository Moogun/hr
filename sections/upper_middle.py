import pandas as pd
import numpy as np
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, \
    QLabel, QFrame, QPushButton, QRadioButton, QTableWidget, QTableWidgetItem

import plotly.graph_objects as go
from PyQt5.QtWebEngineWidgets import QWebEngineView

from network.tr_val import Tr_Val
import time

class UpperMiddle(QFrame):
    def __init__(self):
        super().__init__()

        # Create the main vertical layout
        vbox = QVBoxLayout(self)

        # Create the first horizontal layout for the label and button
        hbox1 = QHBoxLayout()

        label = QLabel('Tr Val')

        # Store tr_val instance in self.tr_val
        # market 0, 1(kospi), 2(kosdaq) -- 0(today), 1(yesterday)
        self.tr_val = Tr_Val('1', '0')

        button = QPushButton('Update')
        button.clicked.connect(self.update_table)
        # button.clicked.connect(self.update_multi_tables)

        self.radio_btn1 = QRadioButton("spi")
        self.radio_btn2 = QRadioButton("daq")
        self.radio_btn1.setChecked(True)

        self.radio_btn1.toggled.connect(self.on_radio_button_toggled)
        self.radio_btn2.toggled.connect(self.on_radio_button_toggled)

        hbox1.addWidget(label)
        hbox1.addWidget(button)
        hbox1.addWidget(self.radio_btn1)
        hbox1.addWidget(self.radio_btn2)

        self.dfs = None
        self.table = QTableWidget(3, 4)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.table)

        # Create hbox3 for the chart
        self.hbox3 = QHBoxLayout()
        self.view = QWebEngineView()

        # Add the horizontal layouts to the main vertical layout
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(self.hbox3)

    def on_radio_button_toggled(self):
        # Update the label text when a radio button is toggled
        if self.radio_btn1.isChecked():
            self.tr_val.set_gubun('1')
        elif self.radio_btn2.isChecked():
            self.tr_val.set_gubun('2')

    def update_multi_tables(self):
        self.update_table(self)

    def refresh(self):
        print('upper middle refresh')
        self.update_table()

    def update_table(self):
        self.dfs = self.tr_val.fetch()
        # Wait for the event to be set
        self.tr_val.event.wait()

        self.table.clear()
        self.dfs = self.dfs.drop(columns=['sign', 'bef_diff', 'filler', 'jnilvolume'])

        # print('update table dfs ', dfs)
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

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

        self.update_chart(self.dfs)

    def update_chart(self, dfs):

        x = dfs['value']
        y = dfs['diff']
        bubble_text = dfs['hname']

        size = np.ceil(pd.to_numeric(dfs['price']) / 20000)
        x = pd.to_numeric(x)
        y = pd.to_numeric(y)

        def get_text_color(y_value):
            return 'red' if y_value > 0 else 'blue'

        fig = go.Figure(
            # data=[go.Bar(y=y, x=x, width=0.1)],
            data =[go.Scatter(y=y,
                              x=x,
                              mode='markers+text',
                              marker=dict(color='gray', size=size, sizemode='diameter'),
                              text=bubble_text,
                              textposition="top center",
                              textfont=dict(size=9, color=[get_text_color(i) for i in y])
                              )],
            layout={
                'margin': {'l': 10, 'r': 10, 't': 30, 'b': 10},  # Minimized margins
                'xaxis': {'showspikes': False,},  # Remove x-axis borders
                'yaxis': {'showspikes': False},  # Remove y-axis borders
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

