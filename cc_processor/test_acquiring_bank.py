import pytest
from acquiring_bank import AcquiringBank
from card import Card

def test_authorize_less_than_ten():
    card_type = "Platinum"
    card_number = 4111111111111111
    spending_limit = 2500
    test_card = Card(card_type, card_number, spending_limit)

    charge_amount = 9.00

    test_bank = AcquiringBank()

    assert test_bank.authorize_transaction(test_card, charge_amount) == True
