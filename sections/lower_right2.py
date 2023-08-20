import pandas as pd
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QFrame, QPushButton, QHBoxLayout, QTableWidgetItem, QTableWidget, QRadioButton, QLineEdit
from network.ready_short import Ready_Short

import plotly.graph_objects as go
from PyQt5.QtWebEngineWidgets import QWebEngineView
from datetime import datetime, timedelta
class LowerRight2(QFrame):
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

        # self.current_datetime = datetime.now()
        # self.today = str(self.current_datetime.date())
        # self.formatted_today = datetime.strptime(self.today, "%Y%m%d")
        #
        # print('today', self.today, self.formatted_today )
        # self.day_300ago = self.current_datetime.date() - timedelta(weeks=60)
        # self.formatted_day_300ago = datetime.strptime(self.day_300ago, "%Y%m%d")

        dt = datetime.now()
        dt_date = str(dt.date())

        today = dt.strptime(dt_date, "%Y-%m-%d")
        sdate = today.strftime("%Y%m%d")
        # sdate = pd.to_numeric(sdate)
        day_300ago = today.date() - timedelta(weeks=60)
        edate = day_300ago.strftime("%Y%m%d")
        print('sdate', sdate, type(sdate), type(edate))

        comp_id = Company().id
        self.ready_short = Ready_Short(comp_id, edate, sdate)

        self.dfs = None
        self.table = QTableWidget(3, 4)
        self.table.setMaximumHeight(200)
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
        self.ready_short.set_shcode(comp_id)

        self.dfs = self.ready_short.fetch()
        # Wait for the event to be set
        self.ready_short.event.wait()

        self.table.clear()

        if self.dfs.empty:
            print("empty data")
        else:
            # self.dfs = self.dfs.drop(columns=['sign'])

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
        y = dfs['price']
        y = pd.to_numeric(y)

        y_bar = dfs['tovolume']
        y_bar = pd.to_numeric(y_bar)

        y_bar2 = dfs['upvolume']
        y_bar2 = pd.to_numeric(y_bar2)

        y_bar3 = dfs['dnvolume']
        y_bar3 = pd.to_numeric(y_bar3)

        fig = go.Figure(
            # data=[go.Bar(y=y, x=x, width=0.1)],
            data=[
                go.Scatter(y=y, x=x, name='price', mode='lines+markers'),
                go.Scatter(x=x, y=y_bar, mode='lines+markers', yaxis='y2', name='remaining', marker=dict(color='gray')),
                go.Bar(x=x, y=y_bar2, name='new', marker=dict(color='lightblue')),
                go.Bar(x=x, y=y_bar3, name='off', marker=dict(color='salmon')),
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
