import pytest
from card import Card
from customer import Customer
from processor import Processor

@pytest.fixture
def card():
    return Card(card_type="TestType", number="7969024409737685", spending_limit=250)

@pytest.fixture
def card_2():
    return Card(card_type="Platinum", number="88778501", spending_limit=500)

def test_customer_default_create():
    customer = Customer(name="Crow T. Robot")
    assert customer.name == "Crow T. Robot"
    assert customer.cards == []

def test_customer_with_card():
    customer = Customer(name="Kirby")
    add_card = customer.add_card("TestType", "7969024409737685", 500)

    assert add_card == True
    assert customer.cards[0].card_type == "TestType"
    assert len(customer.cards) == 1
    assert customer.cards[0].spending_limit == 500
    assert customer.cards[0].number == "7969024409737685"

def test_customer_create_with_card(card):
    customer = Customer(name="Ness", cards=[card])
    # we're passing the test fixture card, which has a spending limit 250

    assert customer.cards[0].number == "7969024409737685"
    assert customer.cards[0].card_type == "TestType"
    assert len(customer.cards) == 1
    assert customer.cards[0].spending_limit == 250

def test_customer_add_additional_card(card, card_2):
    customer = Customer(name="Akechi", cards = [card, card_2])

    assert customer.cards[0].number == "7969024409737685"
    assert customer.cards[0].card_type == "TestType"
    assert customer.cards[0].spending_limit == 250

    assert customer.cards[1].number == "88778501"
    assert customer.cards[1].card_type == "Platinum"
    assert customer.cards[1].spending_limit == 500

    assert len(customer.cards) == 2

def test_get_card_with_type(card, card_2):
    customer = Customer(name="Fry", cards = [card, card_2])

    assert customer.get_card("Platinum") == card_2
