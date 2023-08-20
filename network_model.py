from network.tr_val import Tr_Val
from network.tr_program import Tr_Program
from network.tr_half_min import Tr_Half_Min
from q_params import Q_Params
from datetime import datetime
import pandas as pd
from network.tr_shcode import Tr_Shcode

class NetworkModel:
    def __init__(self):
        self.p_instance = Q_Params()

    # market 0, 1(kospi), 2(kosdaq) -- 0(today), 1(yesterday)
    def fetch_tr_val(self):
        if self.p_instance.market == "p":
            self.tr_val = Tr_Val('1', '0')
        else:
            self.tr_val = Tr_Val('2', '0')

        self.dfs = self.tr_val.fetch()

        current_time = datetime.now()
        formatted_time = current_time.strftime("%H:%M:%S")
        self.dfs['time'] = formatted_time

        self.tr_val.event.wait()
        return self.dfs

    def fetch_tr_pro(self):

        # 0 kospi, 1 kosdaq
        # 0 수량, 1 금액
        # 0 시총, 1, 순매수, 2, 순매도, 3 매도, 4, 매수

        if self.p_instance.market == "p":
            self.tr_pro = Tr_Program('0', '0', '0')
        else:
            self.tr_pro = Tr_Program('1', '0', '0')

        self.dfs = self.tr_pro.fetch()

        # current_time = datetime.now()
        # formatted_time = current_time.strftime("%H:%M:%S")
        # self.dfs['time'] = formatted_time

        self.tr_pro.event.wait()
        return self.dfs

    def fetch_tr_half_min(self):
        sh = self.p_instance.shcode

        try:
            if sh is not None:
                print('sh ', sh)
                self.tr_half_min = Tr_Half_Min(sh)
            else:
                print('sh ', sh, '- samsung')
                self.tr_half_min = Tr_Half_Min('005930')
        except:
            print('Cause ? ')

        try:
            self.dfs = self.tr_half_min.fetch()
            print('second try --- 1')
            self.tr_pro.event.wait()
        except:
            print('second try block ')
        return self.dfs
