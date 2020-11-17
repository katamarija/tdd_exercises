class Merchant:
    def __init__(self, name):
        self._name = name
        self._customers = {}

    def add_customer(self, customer):
        self._customers[customer.name] = customer

    def get_customer(self, customer_name):
        if customer_name not in self._customers:
            return None
        return self._customers[customer_name]

