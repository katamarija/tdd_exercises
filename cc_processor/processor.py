from customer import Customer

class Processor:
    def __init__(self):
        self.customers = []

    def process(self, input_str):
        command = input_str.split()[0]
        customer_name = input_str.split()[1]

        if command == "Add":
            card_number = input_str.split()[2]
            amount = int(input_str.split()[3].strip('$'))
            customer = Customer(name=customer_name)

            self.customers.append(customer)

            spending_limit = amount
            customer.add_card(card_number, spending_limit)
        elif command == "Charge":
            amount = int(input_str.split()[2].strip('$'))
            for customer in self.customers:
                if customer.name == customer_name:
                    customer.cards[0].charge(amount)
        elif command == "Refund":
            amount = int(input_str.split()[2].strip('$'))
            for customer in self.customers:
                if customer.name == customer_name:
                    customer.cards[0].refund(amount)
        else:
            print("Invalid")
            pass

    def print_current_balances(self):
        for customer in sorted(self.customers, key=lambda customer: customer.name):
            if customer.cards[0].valid == True:
                print(f"{customer.name}: ${customer.cards[0].balance}")
            else:
                print(f"{customer.name}: error")

    # def _key(customer):
    #     return customer.name
    #
    # customerA < customerB
    #
    # key(customerA) < key(customerB)
    # customer.name < customer.name
