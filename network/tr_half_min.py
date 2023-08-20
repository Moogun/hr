from pyxing.query import *
import threading
import time
class Tr_Half_Min:

    def __init__(self, shcode):
        print("Tr_Half_Min")
        self.shcode = shcode #
        self.event = threading.Event()

    def fetch(self):
        xaquery = XAQuery()
        dfs = xaquery.block_request("t1302", shcode=self.shcode)
        self.event.set() # Signal that dfs has been filled
        print('dfs half min', dfs)
        return dfs[0]

    def set_shcode(self, shcode):
        print('tr_Half_Min', shcode)
        self.shcode = shcode


