from pyxing.query import *
import threading

class Cap:

    def __init__(self, gubun, jnilgubun):
        print("Cap")
        self.gubun = gubun
        self.jnilgubun = jnilgubun
        self.event = threading.Event()

    def fetch(self):
        xaquery = XAQuery()
        dfs = xaquery.block_request("t1463", gubun=self.gubun, jnilgubun=self.jnilgubun)
        self.event.set() # Signal that dfs has been filled
        return dfs[1]
