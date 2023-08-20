class Model:
    def __init__(self):
        self.data = 0
        self.tr_val = None
        self.tr_pro = None
        self.tr_live_30s = None


    # BOX3
    def set_tr_val(self, value):
        self.tr_val = value

    def get_tr_val(self):
        return self.tr_val

    # BOX5
    def set_tr_pro(self, value):
        self.tr_pro = value

    def get_tr_pro(self):
        return self.tr_pro


    # BOX4
    def set_tr_half_min(self, value):
        self.tr_half_min = value

    def get_tr_half_min(self):
        return self.tr_half_min
