from card import Card

class Customer:
    def __init__(self, name, cards=None):
        self.name = name
        self.cards = cards if cards != None else []
        # self.cards = cards || []

    def add_card(self, card_number, spending_limit):
        new_card = Card(card_number, spending_limit)
        self.cards.append(new_card)
        return True