import pandas as pd
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QFrame, QPushButton, QHBoxLayout, QTableWidgetItem, QTableWidget, QRadioButton, QLineEdit
from network.tr_shcode_days import Tr_Shcode_Days
from company import Company

import plotly.graph_objects as go
from PyQt5.QtWebEngineWidgets import QWebEngineView

class UpperRight2(QFrame):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout(self)

        # Create the first horizontal layout for the label and button
        hbox1 = QHBoxLayout()

        button = QPushButton('Update')
        button.clicked.connect(self.update_table)

        # # self.radio_btn1 = QRadioButton("time")
        # # self.radio_btn2 = QRadioButton("days")
        # # self.radio_btn1.setChecked(True)
        #
        # # self.radio_btn1.toggled.connect(self.on_radio_button_toggled)
        # # self.radio_btn2.toggled.connect(self.on_radio_button_toggled)

        hbox1.addWidget(button)
        # hbox1.addWidget(self.radio_btn1)
        # hbox1.addWidget(self.radio_btn2)

        # data
        print('u_right Shcode.id', Company().id)
        comp_id = Company().id
        self.tr_shcode_days = Tr_Shcode_Days(comp_id)

        self.dfs = None
        self.table = QTableWidget(3, 4)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.table)

        self.hbox3 = QHBoxLayout()
        self.view = QWebEngineView()

        # Add the horizontal layouts to the main vertical layout
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(self.hbox3)

    # def on_radio_button_toggled(self):
    #     if self.radio_btn1.isChecked():
    #         self.tr_pro_shcode.set_gubun2('0')
    #     elif self.radio_btn2.isChecked():
    #         self.tr_pro_shcode.set_gubun2('1')

    def refresh(self):
        print('upper middle refresh')
        shcode = Company().id
        if len(shcode) > 5:
            self.update_table()
        else:
            print('no valid shcode')
    def update_table(self):
        comp_id = Company().id
        self.tr_shcode_days.set_shcode(comp_id)

        self.dfs = self.tr_shcode_days.fetch()
        # Wait for the event to be set
        self.tr_shcode_days.event.wait()

        self.table.clear()
        print('self. dfs', self.dfs)

        if self.dfs.empty:
            print("empty data")
        else:
            self.dfs = self.dfs.drop(columns=['sign'])

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
        x = dfs['date']
        y = dfs['close']
        y = pd.to_numeric(y)

        y_bar = dfs['volume']
        y_bar = pd.to_numeric(y_bar)

        fig = go.Figure(
            # data=[go.Bar(y=y, x=x, width=0.1)],
            data=[
                go.Scatter(y=y, x=x, name='price', mode='lines+markers'),
                go.Bar(x=x, y=y_bar, yaxis='y2', name='volume', marker=dict(color='gray'))
            ],
            layout={
                'margin': {'l': 10, 'r': 10, 't': 30, 'b': 10},  # Minimized margins
                'xaxis': {'showspikes': False, 'autorange': 'reversed'},  # Remove x-axis borders
                'yaxis': {'showspikes': False},
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
        self.hbox3.addWidget(self.view)
