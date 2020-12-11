import pytest
from customer import Customer
from gateway import Gateway
from merchant import Merchant

@pytest.fixture
def gateway():
    return Gateway()

def test_merchant_can_add_customer(gateway):
    merchant_name = "Planet Express"
    customer_name = "Philip J Fry"
    test_merchant = gateway.create_merchant(merchant_name)

    assert gateway.merchant_add_customer(merchant_name, customer_name) == True
    customer = test_merchant.get_customer(customer_name)
    assert customer.name == customer_name

# Can split this into more targeted tests
def test_merchant_can_charge_customer(gateway):
    merchant_name = "Planet Express"
    customer_name = "Philip J Fry"
    test_merchant = gateway.create_merchant(merchant_name)
    card_type = "Platinum"
    card_number = 4111111111111111
    charge_amount = 9.00
    spending_limit = 2500

    assert gateway.merchant_charge_customer(merchant_name, customer_name, card_type, card_number, charge_amount, spending_limit) == True

    assert len(test_merchant.customers) == 1
    customer = test_merchant.get_customer(customer_name)
    assert customer.get_card(card_type).balance == 9.00

    assert gateway.merchant_charge_customer(merchant_name, customer_name, card_type, card_number, charge_amount, spending_limit) == True

    assert len(test_merchant.customers) == 1
    customer = test_merchant.get_customer(customer_name)
    assert customer.get_card(card_type).balance == 18.00

def test_declined_charge(gateway):
    merchant_name = "Planet Express"
    customer_name = "Philip J Fry"
    test_merchant = gateway.create_merchant(merchant_name)
    card_type = "Platinum"
    card_number = 4111111111111111
    charge_amount = 25.00
    spending_limit = 2500

    assert gateway.merchant_charge_customer(merchant_name, customer_name, card_type, card_number, charge_amount, spending_limit) == False
    customer = test_merchant.get_customer(customer_name)
    assert customer.get_card(card_type).balance == 0

def test_merchant_can_refund_customer(gateway):
    merchant_name = "Planet Express"
    customer_name = "Philip J Fry"
    test_merchant = gateway.create_merchant(merchant_name)
    card_type = "Platinum"
    card_number = 4111111111111111
    refund_amount = 25.00
    spending_limit = 2500

    assert gateway.merchant_refund_customer(merchant_name, customer_name, card_type, card_number, refund_amount, spending_limit) == True
    customer = test_merchant.get_customer(customer_name)
    assert customer.get_card(card_type).balance == -25.00
