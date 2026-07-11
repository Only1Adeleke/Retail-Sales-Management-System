import pytest

from inventory import add_product
from sales import sell_product, total_sales


def test_sell_and_total():
    inv = {}
    sales = []
    add_product(inv, "s1", "Pen", 2.0, 10)
    amt = sell_product(inv, sales, "s1", 2, 10)
    assert round(amt, 2) == 3.60  # 4.0 with 10% off
    assert inv["s1"]["stock"] == 8
    assert total_sales(sales) == pytest.approx(3.6)


def test_sell_insufficient_stock():
    inv = {}
    sales = []
    add_product(inv, "s2", "Eraser", 1.0, 1)
    with pytest.raises(ValueError):
        sell_product(inv, sales, "s2", 2, 0)


def test_sell_invalid_inputs():
    inv = {}
    sales = []
    add_product(inv, "s3", "Ruler", 3.0, 5)
    with pytest.raises(ValueError):
        sell_product(inv, sales, "s3", 0, 0)
    with pytest.raises(KeyError):
        sell_product(inv, sales, "missing", 1, 0)
    with pytest.raises(ValueError):
        sell_product(inv, sales, "s3", 1, -5)
    with pytest.raises(ValueError):
        sell_product(inv, sales, "s3", 1, 150)


def test_discount_boundary_100():
    inv = {}
    sales = []
    add_product(inv, "s4", "Marker", 5.0, 2)
    amt = sell_product(inv, sales, "s4", 1, 100)
    assert amt == 0.0
