from customer import Customer

class Processor:
    def __init__(self):
        self.customers = {}

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
                self.customers[customer_name] = customer
            customer.add_card(card_type, card_number, spending_limit)
        elif command == "Charge":
            amount = int(input_str.split()[3].strip('$'))
            customer = self.get_customer(customer_name)
            customer.get_card(card_type).charge(amount)
        elif command == "Refund":
            amount = int(input_str.split()[3].strip('$'))
            customer = self.get_customer(customer_name)
            customer.get_card(card_type).refund(amount)
        else:
            print("Invalid")
            pass

    def print_current_balances(self):
        for customer_name in sorted(self.customers):
            customer = self.customers[customer_name]

            print(f"{customer.name}: ", end="")
            for card_type in sorted(customer.cards):
                card = customer.get_card(card_type)
                if card.valid == True:
                    print(f"({card.card_type}) ${card.balance}, ", end="")
                else:
                    print(f"({card.card_type}) error, ", end="")
            print()

    def get_customer(self, customer_name):
        if customer_name not in self.customers:
            return None

        return self.customers[customer_name]
