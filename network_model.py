from network.tr_val import Tr_Val
from q_params import Q_Params
from datetime import datetime
import pandas as pd

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
