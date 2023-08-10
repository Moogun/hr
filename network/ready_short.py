from pyxing.query import *
import threading
import time

from datetime import datetime, timedelta
class Ready_Short:

    def __init__(self, shcode, start_date, end_date):
        print("Ready_Short")
        self.shcode = shcode #
        self.start_date = start_date
        self.end_date = end_date
        self.event = threading.Event()

    def fetch(self):
        xaquery = XAQuery()
        dfs = xaquery.block_request("t1941", shcode=self.shcode, sdate=self.start_date, edate=self.end_date)
        print('ready short dfs', dfs)
        self.event.set() # Signal that dfs has been filled
        print('dfs[0]', dfs[0])
        return dfs[0]

    def set_shcode(self, shcode):
        print('Ready_Short', shcode)
        self.shcode = shcode

