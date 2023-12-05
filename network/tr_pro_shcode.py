from pyxing.query import *
import threading
class Tr_Pro_Shcode:

    def __init__(self, gubun1, gubun2, shcode):
        print("Tr_Pro_Shcode shcode", shcode)
        self.gubun1 = gubun1 # 0 수량, 1 금액
        self.gubun2 = gubun2 # 0 시간, 1, 일별,
        self.shcode = shcode
        self.event = threading.Event()

    def fetch(self):
        xaquery = XAQuery()
        dfs = xaquery.block_request("t1637", gubun1=self.gubun1, gubun2=self.gubun2, shcode=self.shcode, cts_idx=9999)
        self.event.set() # Signal that dfs has been filled
        print('pr shcode fetch dfs', dfs[0])
        print('pr shcode fetch dfs', dfs[1])
        return dfs[1]

    def set_gubun2(self, gubun2):
        self.gubun2 = gubun2

    def set_shcode(self, shcode):
        self.shcode = shcode

