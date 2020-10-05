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

def test_customer_default_create():
    customer = Customer(name="Crow T. Robot")
    assert customer.name == "Crow T. Robot"
    assert customer.cards == []

def test_customer_with_card():
    customer = Customer(name="Kirby")
    add_card = customer.add_card("7969024409737685", 500)
    assert add_card == True
    assert len(customer.cards) == 1
    assert customer.cards[0].spending_limit == 500
    assert customer.cards[0].number == "7969024409737685"

def test_customer_create_with_card(card):
    customer = Customer(name="Ness", cards=[card])
    # we're passing the test fixture card, which has a spending limit 250

    assert len(customer.cards) == 1
    assert customer.cards[0].spending_limit == 250

