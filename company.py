class Company:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.id = "00"
        return cls._instance

    def update_id(self, id=None):
        self.id = id