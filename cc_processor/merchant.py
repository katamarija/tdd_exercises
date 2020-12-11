from acquiring_bank import AcquiringBank

class Merchant:
    def __init__(self, name):
        self._name = name
        self._customers = {}
        self._bank = AcquiringBank()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def customers(self):
        return self._customers

    def add_customer(self, customer):
        self._customers[customer.name] = customer

    def get_customer(self, customer_name):
        if customer_name not in self._customers:
            return None
        return self._customers[customer_name]

    def get_bank(self):
        return self._bank
