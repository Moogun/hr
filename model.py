class Model:
    def __init__(self):
        self.data = 0
        self.tr_val = None

    def set_tr_val(self, value):
        self.tr_val = value

    def get_tr_val(self):
        return self.tr_val