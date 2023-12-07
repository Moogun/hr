import pandas as pd
class Controller:
    def __init__(self, model, network_model):
        print('controller')
        self.model = model
        self.network_model = network_model

    def set_view(self, view):
        self.view = view

    def ask_tr_future(self):
        data = self.network_model.fetch_tr_future()
        print('ask_tr_future data', data)
        self.model.set_tr_future(data)
        self.view.update_tr_future()

    def ask_tr_days(self):
        data = self.network_model.fetch_tr_days()
        self.model.set_tr_days(data)
        self.view.update_tr_days()

    def ask_tr_val(self):
        # date check, today is 230801,
        # dates = [ 230801.csv, 230731, 230730 ]
        # if dates.contain(today), overwrite ? :
        # else : just load
        data = self.network_model.fetch_tr_val()
        # data.to_csv('val.csv', index=False) # Set index=False to avoid writing row numbers as a separate column
        self.model.set_tr_val(data)
        self.view.update_tr_val()

    def ask_tr_pro(self):
        data = self.network_model.fetch_tr_pro()
        self.model.set_tr_pro(data)
        self.view.update_tr_pro()

    def ask_tr_pro_shcode(self):
        data = self.network_model.fetch_tr_pro_shcode()
        print('ask tr shcode', data)
        self.model.set_tr_pro_shcode(data)
        self.view.update_tr_pro_shcode()

    def ask_tr_half_min(self):
        data = self.network_model.fetch_tr_half_min()
        self.model.set_tr_half_min(data)
        self.view.update_tr_half_min()

    def ask_ready_short(self):
        data = self.network_model.fetch_ready_short()
        self.model.set_ready_short(data)
        self.view.update_ready_short()

    def ask_tr_today(self):
        data = self.network_model.fetch_tr_today()
        self.model.set_tr_today(data)
        self.view.update_tr_today()

