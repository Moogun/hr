class Q_Params:
    _instance = None

    def __init__(self, shcode=None, focode=None, market='p', next=None):
        self.shcode = shcode
        self.focode = focode
        self.market = market
        self.next = next

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def set_shcode(self, shcode):
        print('set_shcode', shcode)
        self.shcode = shcode

    def set_focode(self, focode):
        print('set_focode', focode)
        self.focode = focode

    def set_market(self, market):
        self.market = market

    def set_next(self, next):
        self.next = next
