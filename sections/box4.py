import pandas as pd
import numpy as np

from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QFrame, QPushButton, QTableWidget, QTableWidgetItem, QRadioButton
import plotly.graph_objects as go
from PyQt5.QtWebEngineWidgets import QWebEngineView

from network.tr_program import Tr_Program
from company import Company

class Box4(QFrame):
    def __init__(self):
        super().__init__()
        # Create the main vertical layout
        vbox = QVBoxLayout(self)

        # Create the first horizontal layout for the label and button
        hbox1 = QHBoxLayout()

        label = QLabel('Program')
        button = QPushButton('Update')
        button.clicked.connect(self.update_table)

        self.radio_btn1 = QRadioButton("spi")
        self.radio_btn2 = QRadioButton("daq")
        self.radio_btn1.setChecked(True)

        self.radio_btn1.toggled.connect(self.on_radio_button_toggled)
        self.radio_btn2.toggled.connect(self.on_radio_button_toggled)

        hbox1.addWidget(label)
        hbox1.addWidget(button)
        hbox1.addWidget(self.radio_btn1)
        hbox1.addWidget(self.radio_btn2)


        # data
        self.tr_program = Tr_Program('0', '1', '1')

        self.dfs = None
        self.table = ClickableTableWidget(3, 4)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.table)

        self.hbox3 = QHBoxLayout()
        self.view = QWebEngineView()

        # Add the horizontal layouts to the main vertical layout
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(self.hbox3)

    def on_radio_button_toggled(self):
        if self.radio_btn1.isChecked():
            self.tr_program.set_gubun('0')
        elif self.radio_btn2.isChecked():
            self.tr_program.set_gubun('1')

    def refresh(self):
        print('upper middle refresh')
        self.update_table()

    def update_table(self):
        self.dfs = self.tr_program.fetch()
        # Wait for the event to be set
        self.tr_program.event.wait()

        self.table.clear()
        print('self. dfs', self.dfs)
        self.dfs = self.dfs.drop(columns=['offervalue', 'stksvalue', 'svolume', 'offervolume', 'stksvolume', 'sgta'])

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
        # x = dfs['svalue']
        # y = dfs['diff']
        # bubble_text = dfs['hname']
        #
        # x = pd.to_numeric(x)
        # y = pd.to_numeric(y)

        x = dfs['hname']

        y = dfs['svalue']
        y_diff = dfs['diff']

        y = pd.to_numeric(y)
        y_diff = pd.to_numeric(y_diff)
        y_diff = np.int64(y_diff)

        def get_text_color(y_value):
            return 'pink' if y_value > 0 else 'cornflowerblue'

        fig = go.Figure(
            data=[
                go.Bar(x=x, y=y, name='val_tick', marker=dict(color='grey')),
                go.Bar(x=x, y=y_diff, name='diff', yaxis='y2', marker=dict(color=[get_text_color(i) for i in y_diff])),
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

class ClickableTableWidget(QTableWidget):
    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        self.initUI()

    def initUI(self):
        # Connect the itemClicked signal to the on_item_clicked method
        self.itemClicked.connect(self.on_item_clicked)

    def on_item_clicked(self, item):
        # Get the row and column index of the clicked item
        row = item.row()
        col = item.column()

        # Get the text of the clicked item
        text = item.text()
        print(f"Clicked cell: Row={row}, Column={col}, Text={text}")

        if len(text) == 6:
            print('assume this is shcode and update other sections ')