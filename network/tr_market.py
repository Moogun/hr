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
                                    gubun1=2,
                                    gubun2=2,
                                    gubun3=2,
                                    gubun4=2,
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


