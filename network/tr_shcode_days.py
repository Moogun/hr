from pyxing.query import *
import threading
import time
class Tr_Shcode_Days:

    def __init__(self, shcode):
        print("Tr_Shcode_Days")
        self.shcode = shcode #
        self.event = threading.Event()

    def fetch(self):
        xaquery = XAQuery()
        dfs = xaquery.block_request("t1305", shcode=self.shcode, dwmcode='1', cnt='300')
        self.event.set() # Signal that dfs has been filled
        return dfs[1]

    def set_shcode(self, shcode):
        print('tr_shcode', shcode)
        self.shcode = shcode

