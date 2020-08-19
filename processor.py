from customer import Customer

class Processor:
    def __init__(self):
        self.customers = []

    def process(self, input_str):
        customer_name = input_str.split()[1]
        customer = Customer(name=customer_name)

        self.customers.append(customer)

        spending_limit = int(input_str.split()[2].strip('$'))
        customer.add_card(spending_limit)
