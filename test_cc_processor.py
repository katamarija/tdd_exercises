import pytest
from card import Card

def test_initial_balance():
    card = Card(spending_limit=5000)
    assert card.balance == 0

def test_spending_limit():
    card = Card(spending_limit=5000)
    assert card.spending_limit == 5000

def test_charge_card():
    card = Card(spending_limit=250)
    card.charge(16)

    assert card.balance == 16

def test_overcharge_card():
    card = Card(spending_limit=1)
    card.charge(1)
    card.charge(1)

    assert card.balance == 1
