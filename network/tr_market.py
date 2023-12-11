from pyxing.query import *
import threading
import time
class Tr_Market:

    def __init__(self):
        print("Tr_Market")
        # self.gubun1 = 1 #
        # self.gubun2 = gubun2 #
        # self.gubun3 = gubun3 #
        # self.gubun4 = gubun4 #
        self.event = threading.Event()

    def fetch(self):
        xaquery = XAQuery()
        dfs = xaquery.block_request("t1601",
                                    # gubun1 = self.gubun1,
                                    # gubun2 = self.gubun2,
                                    # gubun3 = self.gubun3,
                                    # gubun4 = self.gubun4,
                                    # 1 vol, 2 value
                                    gubun1=2, # 금액 2
                                    gubun2=2, # 계약수 1 선물,옵션 금액인지 확인 불가, 숫자 않 맞음
                                    gubun3=2, # 사용x
                                    gubun4=2, # 계약수 1 not working 선물,옵션 금액인지 확인 불가, 숫자 않 맞음
                                    )
        self.event.set() # Signal that dfs has been filled
        print('dfs Tr_Market ', dfs)
        return dfs

    # def set_gubun1(self, gubun1):
    #     self.gubun1 = gubun1
    #
    # def set_gubun2(self, gubun2):
    #     self.gubun2 = gubun2
    #
    # def set_gubun3(self, gubun3):
    #     self.gubun3 = gubun3
    #
    # def set_gubun4(self, gubun4):
    #     self.gubun4 = gubun4


