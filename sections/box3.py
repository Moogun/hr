import pandas as pd
from PyQt5.QtWidgets import QVBoxLayout,  \
    QLabel, QFrame, QTableWidget, QTableWidgetItem, QAbstractItemView, QDesktopWidget
from PyQt5.QtGui import QColor
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from PyQt5.QtWebEngineWidgets import QWebEngineView
from color_book import color_dict
from q_params import Q_Params
from PyQt5.QtGui import QFont, QBrush
from PyQt5.QtCore import Qt

class Box3(QFrame):

    def __init__(self, model):
        super().__init__()
        self.p_instance = Q_Params()
        self.model = model
        self.dfs = None
        self.view = QWebEngineView()

        vbox = QVBoxLayout(self)

        vbox1 = QVBoxLayout()
        label = QLabel('BOX-3 TR VAL')
        vbox1.addWidget(label)

        self.table = QTableWidget(1, 1)
        self.font = QFont()
        self.font.setPointSize(8)

        vbox1.addWidget(self.table)

        vbox.addLayout(vbox1)

    def update_tr_val(self):
        # # Set the selection behavior to highlight the entire row
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.itemSelectionChanged.connect(self.row_selected)  # Connect the signal

        self.dfs = self.model.get_tr_val()
        print('--', self.dfs)

        if self.dfs is not None:
            self.table.clear()

            # csp_path = 'val.csv'
            # self.dfs.to_csv(csp_path, index=False)

            self.dfs = self.dfs.drop(columns=['sign', 'bef_diff', 'filler'])

            num_rows, num_cols = self.dfs.shape
            self.table.setRowCount(num_rows)
            self.table.setColumnCount(num_cols)

            self.table.setHorizontalHeaderLabels(list(self.dfs.columns))

            for row in range(num_rows):
                cell_value = pd.to_numeric(self.dfs.loc[row, 'diff'])
                for col in range(num_cols):
                    item = QTableWidgetItem(str(self.dfs.iloc[row][col]))
                    item.setFont(self.font)

                    if 0 > cell_value :
                        item.setForeground(QBrush(Qt.blue))
                    elif 0 < cell_value:
                        item.setForeground(QBrush(Qt.darkRed))

                    self.table.setItem(row, col, item)

            self.color_rows(num_rows, num_cols)

            self.table.resizeColumnsToContents()
            self.table.resizeRowsToContents()

    def update_tr_vol(self):
        self.dfs = self.model.get_tr_vol()
        print('-- VOLUME', self.dfs)

    def color_rows(self, num_rows, num_cols):
        for row in range(num_rows):
            cell_value = pd.to_numeric(self.dfs.loc[row, 'diff'])
            # if 10 <= cell_value < 20:
            #     self.color_row(row, color_dict['gray1']) # whitesmoke
            # elif 20 <= cell_value < 1000:
            #     self.color_row(row, color_dict['gray3']) # lightGray
            if 10 <= cell_value:
                self.color_row(row, color_dict['gray3']) # lightGray

    def color_row(self, row, color):
        row_items = [self.table.item(row, col) for col in range(self.table.columnCount())]
        for item in row_items:
            item.setBackground(color)

    def row_selected(self):
        selected_rows = self.table.selectionModel().selectedRows()

        if selected_rows:
            selected_row = selected_rows[0].row()
            selected_data = self.dfs.iloc[selected_row]
            # print("Selected Row Data:", selected_data['shcode'])
            if selected_data['shcode'] is not None:
                shcode = selected_data['shcode']
                print('Selected Row Data', shcode)
                self.p_instance.shcode = shcode

    # self.update_chart(self.dfs)

    # def update_multi_tables(self):
    #     self.update_table(self)

    # def refresh(self):
    #     print('upper middle refresh')
    #     self.update_table()
    #
    # def update_table(self):
    #     self.dfs = self.tr_val.fetch()
    #     # Wait for the event to be set
    #     self.tr_val.event.wait()
    #


    # def update_chart(self, dfs):
    #
    #     # x = dfs['value']
    #     # y = dfs['diff']
    #     # bubble_text = dfs['hname']
    #
    #     x = dfs['hname']
    #
    #     y = dfs['value']
    #     y_2 = dfs['jnilvalue']
    #     y_diff = dfs['diff']
    #     print('y_diff before', y_diff)
    #     # size = np.ceil(pd.to_numeric(dfs['price']) / 20000)
    #
    #     # x = pd.to_numeric(x)
    #     y = pd.to_numeric(y)
    #     y_2 = pd.to_numeric(y_2)
    #
    #     y_diff = pd.to_numeric(y_diff)
    #     y_diff = np.int64(y_diff)
    #
    #     def get_text_color(y_value):
    #         return 'pink' if y_value > 0 else 'cornflowerblue'
    #
    #     fig = go.Figure(
    #         data =[
    #             go.Bar(x=x, y=y, name='val_to', marker=dict(color='grey')),
    #             go.Bar(x=x, y=y_2, name='val_ye', marker=dict(color='tan')),
    #             go.Bar(x=x, y=y_diff, name='diff', yaxis='y2', marker=dict(color=[get_text_color(i) for i in y_diff])), #
    #         ],
    #
    #         layout={
    #             'margin': {'l': 10, 'r': 10, 't': 30, 'b': 10},  # Minimized margins
    #             'xaxis': {'showspikes': False, },
    #             'yaxis': {'showspikes': False, },
    #             'yaxis2': {'showspikes': False, 'overlaying': 'y', 'side': 'right',},
    #         }
    #     )
    #
    #     # Convert the Plotly chart to HTML
    #     raw_html = '<html><head><meta charset="utf-8" /></head><body style="margin:0; padding:0;>'
    #     content = fig.to_html(full_html=False, include_plotlyjs='cdn')
    #     raw_html += content.replace("window.PlotlyConfig = {MathJaxConfig: 'local'};", "")
    #     raw_html += '</body></html>'
    #
    #     # Set up the QWebEngineView
    #     self.view.setHtml(raw_html)
    #     self.hbox3.addWidget(self.view)

