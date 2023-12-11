from pyxing.query import *
import threading
import asyncio

class Tr_Vol:
    def __init__(self, gubun, jnilgubun):
        print('Tr_Vol')
        self.gubun = gubun
        self.jnilgubun = jnilgubun
        self.event = threading.Event()

    def fetch(self):
        print('Tr_Vol fetch self.gubun jnilgubun', self.gubun, self.jnilgubun)
        xaquery = XAQuery()

        idx = int(40)
        dfs = xaquery.block_request("t1452_2", gubun=self.gubun, jnilgubun=self.jnilgubun, idx=idx)
        self.event.set() # Signal that dfs has been filled

        return dfs[1]

    def set_gubun(self, gubun):
        self.gubun = gubun

    def set_jnilgubun(self, jnilgubun):
        self.jnilgubun = jnilgubun