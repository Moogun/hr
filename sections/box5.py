from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, \
    QLabel, QFrame, QPushButton, QRadioButton, QTableWidget, QTableWidgetItem
import pandas as pd
from color_book import color_dict

class Box5(QFrame):
    def __init__(self, model):
        super().__init__()
        self.model = model

        vbox = QVBoxLayout(self)

        vbox1 = QVBoxLayout()
        label = QLabel('PROG')
        vbox1.addWidget(label)

        self.table = QTableWidget(3, 4)
        vbox1.addWidget(self.table)

        vbox.addLayout(vbox1)

    def update_tr_pro(self):
        self.dfs = self.model.get_tr_pro()
        print('view update_tr_pro', self.dfs)

        # csp_path = 'pro.csv'
        # self.dfs.to_csv(csp_path, index=False)

        if self.dfs is not None:
            self.table.clear()

            a = pd.to_numeric(self.dfs['stksvolume'])
            b = pd.to_numeric(self.dfs['offervolume'])
            c = pd.to_numeric(self.dfs['volume'])
            self.dfs['sell_ratio'] = (b/c).round(2)
            self.dfs['buy_ratio'] = (a/c).round(2)

            tril = 1000000000000
            self.dfs['sgta'] = (pd.to_numeric(self.dfs['sgta']) / tril).round(2)
            self.dfs = self.dfs.drop(columns=['svalue', 'offervalue', 'stksvalue', 'sign'])

            num_rows, num_cols = self.dfs.shape
            self.table.setRowCount(num_rows)
            self.table.setColumnCount(num_cols)

            self.table.setHorizontalHeaderLabels(list(self.dfs.columns))

            for row in range(num_rows):
                for col in range(num_cols):
                    item = QTableWidgetItem(str(self.dfs.iloc[row][col]))
                    self.table.setItem(row, col, item)

            self.color_rows(num_rows, num_cols)

            self.table.resizeColumnsToContents()
            self.table.resizeRowsToContents()

    def color_rows(self, num_rows, num_cols):
        for row in range(num_rows):
            cell_value = pd.to_numeric(self.dfs.loc[row, 'diff'])
            if 0 <= cell_value < 3:
                self.color_row(row, color_dict['lavender'])
            elif 3 <= cell_value < 7:
                self.color_row(row, color_dict['thistle'])
            elif 7 <= cell_value < 1000:
                self.color_row(row, color_dict['plum'])

    def color_row(self, row, color):
        row_items = [self.table.item(row, col) for col in range(self.table.columnCount())]
        for item in row_items:
            item.setBackground(color)