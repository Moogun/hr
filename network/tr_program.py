from pyxing.query import *
import threading

class Tr_Program:
    def __init__(self, gubun, gubun1, gubun2):
        print('Tr_Program')
        self.gubun = gubun # 0 kospi, 1 kosdaq
        self.gubun1 = gubun1 # 0 수량, 1 금액
        self.gubun2 = gubun2 # 0 시총, 1, 순매수, 2, 순매도, 3 매도, 4, 매수
        self.event = threading.Event()

    def fetch(self):
        xaquery = XAQuery()
        dfs = xaquery.block_request("t1636", gubun=self.gubun, gubun1 = self.gubun1, gubun2 = self.gubun2)
        self.event.set() # Signal that dfs has been filled
        return dfs[1]

    def set_gubun(self, gubun):
        self.gubun = gubun

    def set_gubun2(self, gubun2):
        self.gubun2 = gubun2
