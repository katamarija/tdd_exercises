from customer import Customer

class Processor:
    def __init__(self):
        self.customers = []

    def process(self, input_str):
        command = input_str.split()[0]
        customer_name = input_str.split()[1]

        if command == "Add":
            card_type = input_str.split()[2]
            card_number = input_str.split()[3]
            amount = int(input_str.split()[4].strip('$'))
            spending_limit = amount
            customer = self.get_customer(customer_name)

            if customer == None:
                customer = Customer(name=customer_name)
                self.customers.append(customer)
                customer.add_card(card_type, card_number, spending_limit)
            else:
                customer.add_card(card_type, card_number, spending_limit)
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

    def get_customer(self, customer_name):
        for customer in self.customers:
            if customer.name == customer_name:
                return customer
