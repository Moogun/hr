class Model:
    def __init__(self):
        self.data = 0
        self.tr_days = None
        self.tr_today = None
        self.tr_val = None
        self.tr_pro = None
        self.tr_half_min = None
        self.tr_pro_shcode = None
        self.ready_short = None

    # BOX1  ------------------------------------------
    def set_tr_future(self, value):
        self.tr_future = value

    def get_tr_future(self):
        return self.tr_future

    # BOX2  ------------------------------------------
    def set_tr_days(self, value):
        self.tr_days = value
    def get_tr_days(self):
        return self.tr_days

    # BOX3  ------------------------------------------
    def set_tr_val(self, value):
        self.tr_val = value

    def get_tr_val(self):
        return self.tr_val

    # BOX5  ------------------------------------------
    def set_tr_pro(self, value):
        self.tr_pro = value

    def get_tr_pro(self):
        return self.tr_pro


    # BOX4  ------------------------------------------
    def set_tr_half_min(self, value):
        self.tr_half_min = value

    def get_tr_half_min(self):
        return self.tr_half_min

    def set_tr_market(self, value):
        self.tr_market = value

    def get_tr_market(self):
        return self.tr_market

            # BOX 6  ------------------------------------------
    def set_tr_pro_shcode(self, value):
        print('setting, ', value)
        self.tr_pro_shcode = value

    def get_tr_pro_shcode(self):
        print('getting ')
        return self.tr_pro_shcode

    # BOX 6  ------------------------------------------
    def set_ready_short(self, value):
        print('setting, ', value)
        self.ready_short = value

    def get_ready_short(self):
        print('getting get_ready_short')
        return self.ready_short


    # BOX 7  ------------------------------------------
    def set_tr_today(self, value):
        print('tr_today setting, ', value)
        self.tr_today = value

    def get_tr_today(self):
        print('getting get_ready_short')
        return self.tr_today

