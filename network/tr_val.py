from pyxing.query import *
import threading
import asyncio

class Tr_Val:
    def __init__(self, gubun, jnilgubun):
        print('Tr_Val')
        self.gubun = gubun
        self.jnilgubun = jnilgubun
        self.event = threading.Event()

    def fetch(self):
        print('tr_val fetch self.gubun jnilgubun', self.gubun, self.jnilgubun)
        xaquery = XAQuery()
        dfs = xaquery.block_request("t1463", gubun=self.gubun, jnilgubun=self.jnilgubun)
        self.event.set() # Signal that dfs has been filled

        return dfs[1]

    def set_gubun(self, gubun):
        self.gubun = gubun

    def set_jnilgubun(self, jnilgubun):
        self.jnilgubun = jnilgubun