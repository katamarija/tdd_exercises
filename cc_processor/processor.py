from customer import Customer

def get_customer_name(customer):
    return customer.name

class Processor:
    def __init__(self):
        self.customers = []

    def process(self, input_str):
        command = input_str.split()[0]
        customer_name = input_str.split()[1]
        card_type = input_str.split()[2]

        if command == "Add":
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
            amount = int(input_str.split()[3].strip('$'))
            for customer in self.customers:
                if customer.name == customer_name:
                    customer.get_card(card_type).charge(amount)
        elif command == "Refund":
            amount = int(input_str.split()[3].strip('$'))
            for customer in self.customers:
                if customer.name == customer_name:
                    customer.get_card(card_type).refund(amount)
        else:
            print("Invalid")
            pass

    def print_current_balances(self):
        for customer in sorted(self.customers, key=get_customer_name):
            print(f"{customer.name}: ", end="")
            for card in sorted(customer.cards, key=lambda card: card.card_type):
                if card.valid == True:
                    print(f"({card.card_type}) ${card.balance}, ", end="")
                else:
                    print(f"({card.card_type}) error, ", end="")
            print()

#    def lambda(customer):
#        return customer.name

# Explanation of sorted in Line 39
#     def _key(customer):
#         return customer.name
#
#     customerA < customerB
#
#     key(customerA) < key(customerB)
#     customer.name < customer.name

    def get_customer(self, customer_name):
        for customer in self.customers:
            if customer.name == customer_name:
                return customer
