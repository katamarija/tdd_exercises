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
    assert customer.cards == {}

def test_customer_with_card():
    customer = Customer(name="Kirby")
    add_card = customer.add_card("TestType", "7969024409737685", 500)

    assert add_card == True
    assert customer.get_card("TestType") != None
    assert len(customer.cards) == 1
    assert customer.get_card("TestType").spending_limit == 500
    assert customer.get_card("TestType").number == "7969024409737685"

def test_customer_create_with_card(card):
    customer = Customer(name="Ness", cards={card.card_type: card})
    # we're passing the test fixture card, which has a spending limit 250

    assert customer.get_card("TestType") != None
    assert customer.get_card("TestType").card_type == "TestType"
    assert len(customer.cards) == 1
    assert customer.get_card("TestType").spending_limit == 250
    assert customer.get_card("TestType").number == "7969024409737685"

def test_customer_add_additional_card(card, card_2):
    cards = {
            card.card_type: card
            , card_2.card_type: card_2
            }
    customer = Customer(name="Akechi", cards = cards)

    assert customer.get_card("TestType") != None
    assert customer.get_card("TestType").spending_limit == 250
    assert customer.get_card("TestType").number == "7969024409737685"
    assert customer.get_card("Platinum") != None
    assert customer.get_card("Platinum").spending_limit == 500
    assert customer.get_card("Platinum").number == "88778501"

    assert len(customer.cards) == 2

def test_get_card_with_type(card, card_2):
    cards = {
            card.card_type: card
            , card_2.card_type: card_2
            }
    customer = Customer(name="Fry", cards = cards)

    assert customer.get_card("Platinum") == card_2
