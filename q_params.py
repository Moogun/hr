class Q_Params:
    _instance = None

    def __init__(self, shcode='None', market='p'):
        self.shcode = shcode
        self.market = market

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def set_shcode(self, shcode):
        self.shcode = shcode

    def set_market(self, market):
        self.market = market
