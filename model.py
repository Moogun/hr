class Model:
    def __init__(self):
        self.data = 0
        self.tr_val = None
        self.tr_pro = None

    def set_tr_val(self, value):
        self.tr_val = value

    def get_tr_val(self):
        return self.tr_val

    def set_tr_pro(self, value):
        self.tr_pro = value

    def get_tr_pro(self):
        return self.tr_pro