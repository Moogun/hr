class Controller:
    def __init__(self, model, network_model):
        print('controller')
        self.model = model
        self.network_model = network_model

    def set_view(self, view):
        self.view = view

    def ask_tr_days(self):
        data = self.network_model.fetch_tr_days()
        self.model.set_tr_days(data)
        self.view.update_tr_days()

    def ask_tr_val(self):
        data = self.network_model.fetch_tr_val()
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

