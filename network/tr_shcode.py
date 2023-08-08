from pyxing.query import *
import threading

class Tr_Shcode:

    def __init__(self, shcode):
        print("Tr_Shcode")
        self.shcode = shcode #
        self.event = threading.Event()

    def fetch(self):
        xaquery = XAQuery()
        dfs = xaquery.block_request("t1302", shcode=self.shcode)
        self.event.set() # Signal that dfs has been filled
        return dfs[1]

    def set_shcode(self, shcode):
        self.shcode = shcode

    def set_cvolume(self, cvolume):
        self.cvolume = cvolume

