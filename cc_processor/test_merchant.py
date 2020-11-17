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
