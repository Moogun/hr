from pyxing.query import *
import threading
import time
class Tr_Today:

    def __init__(self, shcode):
        print("Tr_Today")
        self.shcode = shcode
        self.event = threading.Event()

    def fetch(self):
        xaquery = XAQuery()
        dfs = xaquery.block_request("t1102", shcode=self.shcode)
        print('dfs[0] --------------------- ---------------------', dfs[0])
        print('dfs[1] len --------------------- ', len(dfs))
        self.event.set() # Signal that dfs has been filled
        return dfs[0]

    def set_shcode(self, shcode):
        print('tr_shcode', shcode)
        self.shcode = shcode
