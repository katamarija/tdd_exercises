import pytest
from customer import Customer
from merchant import Merchant

@pytest.fixture
def merchant():
    return Merchant(name="Magic Merchant")

def test_merchant_can_add_customer(merchant):
    customer = Customer(name="Magician")
    merchant.add_customer(customer)
    assert merchant.get_customer(customer.name) == customer

def test_can_get_merchant_name(merchant):
    # assert merchant.get_name() == "Magic Merchant"
    assert merchant.name == "Magic Merchant"


def test_can_set_merchant_name(merchant):
    # assert merchant.set_name("Not-so-magic Merchant") == "Not-so-magic Merchant"
    merchant.name = "Not-so-magic Merchant"
    assert merchant.name == "Not-so-magic Merchant"
