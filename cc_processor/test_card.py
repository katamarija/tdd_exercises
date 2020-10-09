import pytest
from card import Card
from customer import Customer
from processor import Processor

@pytest.fixture
def card():
    return Card(number="7969024409737685", spending_limit=250)

def get_single_card_from_customer(processor, name):
    customer = next(filter(lambda c: c.name == name, processor.customers))
    return customer.cards[0]

def test_initial_balance(card):
    assert card.balance == 0

def test_spending_limit(card):
    assert card.spending_limit == 250

def test_charge_card(card):
    card_charge = card.charge(16)
    assert card.balance == 16
    assert card_charge == True

def test_overcharge_card(card):
    card.charge(250)
    card_overcharge = card.charge(1)
    assert card.balance == 250
    assert card_overcharge == False

def test_refund_card(card):
    card_refund = card.refund(100)
    assert card.balance == -100
    assert card_refund == True

def test_valid_luhn_number():
    assert Card._luhn_valid("1635136358093212") == True

def test_invalid_luhn_number():
    assert Card._luhn_valid("4111111111111112") == False

def test_valid_short_luhn_number():
    assert Card._luhn_valid("349") == True

def test_valid_long_luhn_number():
    assert Card._luhn_valid("5523104176235661500") == True
