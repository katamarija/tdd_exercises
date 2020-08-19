import pytest
from card import Card
from customer import Customer
from processor import Processor

@pytest.fixture
def card():
    return Card(spending_limit=250)

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

def test_customer_default_create():
    customer = Customer(name="Crow T. Robot")
    assert customer.name == "Crow T. Robot"
    assert customer.cards == []

def test_customer_with_card():
    customer = Customer(name="Kirby")
    add_card = customer.add_card(500)
    assert add_card == True
    assert len(customer.cards) == 1
    assert customer.cards[0].spending_limit == 500

def test_customer_create_with_card(card):
    customer = Customer(name="Ness", cards=[card])
    # we're passing the test fixture card, which has a spending limit 250

    assert len(customer.cards) == 1
    assert customer.cards[0].spending_limit == 250

def test_processor_can_create_customer_with_card():
    input_str_1 = "Add Tom $1000"
    input_str_2 = "Add Mary $5"
    # future command: "Charge Tom $5"
    # future command: "Refund Tom $99"

    processor = Processor()

    processor.process(input_str_1)
    processor.process(input_str_2)

    assert len(processor.customers) == 2
    customer_tom = next(filter(lambda c: c.name == "Tom", processor.customers))
    customer_mary = next(filter(lambda c: c.name == "Mary", processor.customers))

    assert customer_tom.name == "Tom"
    assert len(customer_tom.cards) == 1
    card_tom = customer_tom.cards[0]
    assert card_tom.spending_limit == 1000

    assert customer_mary.name == "Mary"
    assert len(customer_mary.cards) == 1
    card_mary = customer_mary.cards[0]
    assert card_mary.spending_limit == 5
