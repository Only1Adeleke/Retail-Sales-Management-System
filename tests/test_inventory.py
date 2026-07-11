import pytest

from inventory import add_product, update_stock, search_product


def test_add_and_search():
    inv = {}
    add_product(inv, "p1", "Apple", 1.25, 10)
    res = search_product(inv, "apple")
    assert len(res) == 1
    assert res[0]["id"] == "p1"


def test_add_invalid():
    inv = {}
    with pytest.raises(ValueError):
        add_product(inv, "", "NoID", 1.0, 1)
    add_product(inv, "p2", "Banana", 0.5, 5)
    with pytest.raises(ValueError):
        add_product(inv, "p2", "Banana2", 0.6, 2)


def test_update_stock():
    inv = {}
    add_product(inv, "p3", "Orange", 0.8, 3)
    new = update_stock(inv, "p3", 2)
    assert new == 5
    new = update_stock(inv, "p3", -1)
    assert new == 4


def test_update_stock_errors():
    inv = {}
    with pytest.raises(KeyError):
        update_stock(inv, "missing", 1)
    add_product(inv, "p4", "Grape", 2.0, 1)
    with pytest.raises(ValueError):
        update_stock(inv, "p4", -5)
