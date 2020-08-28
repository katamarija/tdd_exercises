from customer import Customer

class Processor:
    def __init__(self):
        self.customers = []

    def process(self, input_str):
        command = input_str.split()[0]
        customer_name = input_str.split()[1]
        amount = int(input_str.split()[2].strip('$'))

        if command == "Add":
            customer = Customer(name=customer_name)

            self.customers.append(customer)

            spending_limit = amount
            customer.add_card(spending_limit)
        elif command == "Charge":
            for customer in self.customers:
                if customer.name == customer_name:
                    customer.cards[0].charge(amount)
        elif command == "Refund":
            for customer in self.customers:
                if customer.name == customer_name:
                    customer.cards[0].refund(amount)
        else:
            print("Invalid")
            pass
