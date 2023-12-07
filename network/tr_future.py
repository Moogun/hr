from pyxing.query import *
import threading
import asyncio

class Tr_Future:
    def __init__(self, focode):
        print('Tr_Future')
        self.focode = focode
        self.event = threading.Event()

    def fetch(self):
        print('tr_futre fetch self.focode', self.focode)
        xaquery = XAQuery()
        dfs = xaquery.block_request("t8402", focode=self.focode)
        self.event.set() # Signal that dfs has been filled
        print('dfs[0]', dfs[0])
        return dfs[0]

    def set_focode(self, focode):
        self.focode = focode
