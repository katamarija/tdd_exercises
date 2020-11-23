from card import Card

class Customer:
    def __init__(self, name, cards=None):
        self._name = name
        self._cards = cards if cards != None else {}
        # self.cards = cards || {}

    @property
    def name(self):
        return self._name

    @property
    def cards(self):
        return self._cards

    def add_card(self, card_type, card_number, spending_limit):
        new_card = Card(card_type, card_number, spending_limit)
        self._cards[card_type] = new_card
        return True

# Assumption: customer will only have unique card types for now
    def get_card(self, card_type):
        if card_type not in self._cards:
            return None
        return self._cards[card_type]
