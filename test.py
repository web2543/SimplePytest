import pytest
import Store

@pytest.fixture
def mystore()->Store.Store:
    store=Store.Store(1)
    store.got_call()
    return store

def test_order(mystore):
    assert mystore.order == 1

def test_order_overflow(mystore):
    with pytest.raises(RuntimeError):
        mystore.got_call()

def test_delivery(mystore):
    mystore.delivery()
    assert mystore.order == 0

def test_delivery_underflow(mystore):
    mystore.delivery()
    with pytest.raises(RuntimeError):
        mystore.delivery()
