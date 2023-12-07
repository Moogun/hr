from network.tr_future import Tr_Future
from network.tr_val import Tr_Val
from network.tr_days import Tr_Days
from network.tr_today import Tr_Today
from network.tr_program import Tr_Program
from network.tr_pro_shcode import Tr_Pro_Shcode
from network.tr_half_min import Tr_Half_Min
from network.tr_market import Tr_Market
from network.ready_short import Ready_Short
from q_params import Q_Params
import pandas as pd
from network.tr_shcode import Tr_Shcode
from datetime import datetime, timedelta

class NetworkModel:
    def __init__(self):
        self.p_instance = Q_Params()

    def fetch_tr_future(self):
        print('fetch_tr_future')
        fo = self.p_instance.focode
        self.tr_future = Tr_Future(fo)
        # else:
        #     self.tr_val = Tr_Future('2', '0')
        #
        self.dfs = self.tr_future.fetch()
        self.tr_future.event.wait()
        return self.dfs

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

    def fetch_tr_pro_shcode(self):
        # 0 수량, 1 금액
        # 0 시간, 1, 일별,

        sh = self.p_instance.shcode
        if sh is not None:
            self.tr_pro_shcode = Tr_Pro_Shcode('0', '0', sh)
        else:
            # 005930 Samsung
            self.tr_pro_shcode = Tr_Pro_Shcode('0', '0', '005930')

        try:
            self.dfs = self.tr_pro_shcode.fetch()
            print('0 ----------------', self.dfs)
            self.tr_pro_shcode.event.wait()
            print('1----------------')
        except:
            print('tr_pro_shcode exception')

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

    def fetch_tr_market(self):
        self.tr_market = Tr_Market()
        self.dfs = self.tr_market.fetch()
        print('fetch_tr_market dfs  ')
        self.tr_market.event.wait()
        return self.dfs

    def fetch_tr_days(self):
        sh = self.p_instance.shcode

        dt = datetime.now()
        dt_date = str(dt.date())

        today = dt.strptime(dt_date, "%Y-%m-%d")
        todt = today.strftime("%Y%m%d")

        thirty_weeks_ago = today.date() - timedelta(weeks=30)
        fromdt = thirty_weeks_ago.strftime("%Y%m%d")

        if sh is not None:
            self.tr_days = Tr_Days(sh, '0', fromdt, todt)
        else:
            print('sh ', sh, '- samsung')
            self.tr_days = Tr_Days('005930', '0', fromdt, todt)

        try:
            self.dfs = self.tr_days.fetch()
            print('tr days second try --- 1', self.dfs)
            self.tr_days.event.wait()
        except:
            print('tr days second try block ')

        return self.dfs


    def fetch_ready_short(self):
        sh = self.p_instance.shcode

        dt = datetime.now()
        dt_date = str(dt.date())

        today = dt.strptime(dt_date, "%Y-%m-%d")
        todt = today.strftime("%Y%m%d")

        thirty_weeks_ago = today.date() - timedelta(weeks=30)
        fromdt = thirty_weeks_ago.strftime("%Y%m%d")

        if sh is not None:
            self.ready_short = Ready_Short(sh, fromdt, todt)
        else:
            print('sh ', sh, '- samsung')
            self.ready_short = Ready_Short('005930', fromdt, todt)

        try:
            self.dfs = self.ready_short.fetch()
            print('ready_short second try --- 1', self.dfs)
            self.tr_days.event.wait()
        except:
            print('ready_short second try block ')

        return self.dfs

    def fetch_tr_today(self):
        sh = self.p_instance.shcode

        if sh is not None:
            self.tr_today = Tr_Today(sh)
        else:
            print('sh ', sh, '- samsung')
            self.tr_today = Tr_Today('005930')

        try:
            self.dfs = self.tr_today.fetch()
            print('ready_short second try --- 1', self.dfs)
            self.tr_today.event.wait()
        except:
            print('ready_short second try block ')

        return self.dfs
