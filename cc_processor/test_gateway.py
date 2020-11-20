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
