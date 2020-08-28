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

def test_processor_can_create_customer_with_card():
    input_str_1 = "Add Tom $1000"
    input_str_2 = "Add Mary $5"

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

def test_processor_can_charge_customer_with_existing_card():
    input_str_1 = "Add Tom $6"
    input_str_2 = "Charge Tom $5"
    input_str_3 = "Charge Tom $1"

    processor = Processor()
    processor.process(input_str_1)
    processor.process(input_str_2)

    card_tom = get_single_card_from_customer(processor, "Tom")

    assert card_tom.balance == 5

    processor.process(input_str_3)

    assert card_tom.balance == 6

def test_processor_can_refund_customer_with_existing_card():
    input_str_1 = "Add Tom $6"
    input_str_2 = "Refund Tom $99"

    processor = Processor()
    processor.process(input_str_1)
    processor.process(input_str_2)

    card_tom = get_single_card_from_customer(processor, "Tom")

    assert card_tom.balance == -99

def test_end_to_end_multiple_customer_input():
    input_strs = [
            "Add Tom $1000",
            "Add Lisa $3000",
            "Add Quincy $2000",
            "Charge Tom $500",
            "Charge Tom $800",
            "Charge Lisa $7",
            "Refund Lisa $100",
            "Refund Quincy $200",
            ]

    processor = Processor()
    for s in input_strs:
        processor.process(s)


    card_tom = get_single_card_from_customer(processor, "Tom")
    card_lisa = get_single_card_from_customer(processor, "Lisa")
    card_quincy = get_single_card_from_customer(processor, "Quincy")

    assert card_tom.balance == 500
    assert card_lisa.balance == -93
    assert card_quincy.balance == -200
