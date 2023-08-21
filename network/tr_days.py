from pyxing.query import *
import threading
import time
class Tr_Days:

    def __init__(self, shcode, gubun, fromdt, todt):
        print("Tr_Days")
        self.shcode = shcode #
        self.gubun = gubun # 0 일별, 1 누적
        self.fromdt = fromdt # 0 일별, 1 누적
        self.todt = todt # 0 일별, 1 누적
        self.event = threading.Event()

    def fetch(self):
        xaquery = XAQuery()
        dfs = xaquery.block_request("t1717", shcode=self.shcode, gubun=self.gubun, fromdt=self.fromdt, todt=self.todt)
        print('dfs[0] --------------------- ---------------------', dfs[0])
        print('dfs[1] len --------------------- ', len(dfs))
        self.event.set() # Signal that dfs has been filled
        return dfs[0]

    def set_shcode(self, shcode):
        print('tr_shcode', shcode)
        self.shcode = shcode
