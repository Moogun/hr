class Controller:
    def __init__(self, model, network_model):
        print('controller')
        self.model = model
        self.network_model = network_model

    def set_view(self, view):
        self.view = view

    def ask_tr_val(self):
        data = self.network_model.fetch_tr_val()
        self.model.set_tr_val(data)
        self.view.update_tr_val()

    def ask_tr_pro(self):
        data = self.network_model.fetch_tr_pro()
        self.model.set_tr_pro(data)
        self.view.update_tr_pro()
