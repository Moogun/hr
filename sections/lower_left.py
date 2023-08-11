import pandas as pd
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QFrame, QPushButton, QTableWidget, QTableWidgetItem, QRadioButton

import plotly.graph_objects as go
from PyQt5.QtWebEngineWidgets import QWebEngineView
class LowerLeft(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("border: 1px solid gray;")
        layout = QVBoxLayout(self)
        label = QLabel('Lower left')
        layout.addWidget(label)

    def refresh(self):
        print('a')