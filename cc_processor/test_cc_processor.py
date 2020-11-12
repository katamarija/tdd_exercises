import pytest
from card import Card
from customer import Customer
from processor import Processor

@pytest.fixture
def card():
    return Card(number="7969024409737685", spending_limit=250)

def test_processor_can_create_customer_with_card():
    input_str_1 = "Add Tom Platinum 4111111111111111 $1000"
    input_str_2 = "Add Tom Silver 4111111111111111 $1000"
    input_str_3 = "Add Mary Gold 5454545454545454 $5"

    processor = Processor()

    processor.process(input_str_1)
    processor.process(input_str_2)
    processor.process(input_str_3)

    assert len(processor.customers) == 2
    customer_tom = processor.get_customer("Tom")
    customer_mary = processor.get_customer("Mary")

    assert customer_tom.name == "Tom"
    assert len(customer_tom.cards) == 2

    card_tom_platinum = customer_tom.get_card("Platinum")
    assert card_tom_platinum.spending_limit == 1000

    card_tom_silver = customer_tom.get_card("Silver")
    assert card_tom_silver.spending_limit == 1000

    assert customer_mary.name == "Mary"
    assert len(customer_mary.cards) == 1
    card_mary = customer_mary.get_card("Gold")
    assert card_mary.spending_limit == 5

def test_processor_can_charge_customer_with_existing_card():
    input_str_1 = "Add Tom Platinum 4111111111111111 $6"
    input_str_2 = "Add Tom Silver 4111111111111111 $6"
    input_str_3 = "Charge Tom Platinum $5"
    input_str_4 = "Charge Tom Silver $1"

    processor = Processor()
    processor.process(input_str_1)
    processor.process(input_str_2)
    processor.process(input_str_3)
    processor.process(input_str_4)

    tom_plat = processor.get_customer("Tom").get_card("Platinum")
    tom_silver = processor.get_customer("Tom").get_card("Silver")

    assert tom_plat.balance == 5
    assert tom_silver.balance == 1

def test_processor_can_refund_customer_with_existing_card():
    input_str_1 = "Add Tom Silver 4111111111111111 $6"
    input_str_2 = "Refund Tom Silver $99"

    processor = Processor()
    processor.process(input_str_1)
    processor.process(input_str_2)

    tom_silver = processor.get_customer("Tom").get_card("Silver")

    assert tom_silver.balance == -99

def test_end_to_end_multiple_customer_input(capsys):
    input_strs = [
        "Add Tom Home 4111111111111111 $1000",
        "Add Tom Work 4012000033330026 $500",
        "Add Lisa Work 5454545454545454 $3000",
        "Add Lisa Gold 4111111111111112 $1000",
        "Add Lisa Platinum 378282246310005 $2000",
        "Charge Tom Home $500",
        "Charge Tom Work $800",
        "Charge Lisa Work $7",
        "Refund Lisa Platinum $100"
    ]

    processor = Processor()
    for s in input_strs:
        processor.process(s)

    tom_home = processor.get_customer("Tom").get_card("Home")
    tom_work = processor.get_customer("Tom").get_card("Work")
    lisa_work = processor.get_customer("Lisa").get_card("Work")
    lisa_gold = processor.get_customer("Lisa").get_card("Gold")
    lisa_plat = processor.get_customer("Lisa").get_card("Platinum")

    processor.print_current_balances()
    captured = capsys.readouterr()

    assert tom_home.balance == 500
    assert tom_work.balance == 0
    assert tom_home.valid == True
    assert tom_work.valid == True
    assert lisa_work.balance == 7
    assert lisa_work.valid == True
    assert lisa_gold.valid == False
    assert lisa_plat.balance == -100
    assert lisa_plat.valid == True

    assert captured.out == "Lisa: (Gold) error, (Platinum) $-100, (Work) $7, \nTom: (Home) $500, (Work) $0, \n"
