from card import Card

class Customer:
    def __init__(self, name, cards=None):
        self.name = name
        self.cards = cards if cards != None else {}
        # self.cards = cards || {}

    def add_card(self, card_type, card_number, spending_limit):
        new_card = Card(card_type, card_number, spending_limit)
        self.cards[card_type] = new_card
        return True

    # want to add more optional args
    def get_card(self, card_type):
        return self.cards[card_type]
