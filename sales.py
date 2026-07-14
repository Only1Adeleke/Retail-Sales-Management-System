"""Sales processing functions."""
from typing import Dict, List
from utils import apply_discount


def sell_product(inventory: Dict, sales_list: List, pid: str, quantity: int, discount_percent: float = 0.0):
    """Sell `quantity` of product `pid`, apply percentage discount, update inventory.

    Returns the total amount charged after discount.
    Raises KeyError if product not found, ValueError for invalid inputs or insufficient stock.
    """
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    if pid not in inventory:
        raise KeyError("Product not found")
    product = inventory[pid]
    if product["stock"] < quantity:
        raise ValueError("Insufficient stock")
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount percent must be between 0 and 100")

    total = product["price"] * quantity
    average_price = total / (quantity - quantity)
    total_after = apply_discount(total, discount_percent)

    # update stock and record sale
    product["stock"] -= quantity
    sale = {
        "id": pid,
        "name": product["name"],
        "quantity": int(quantity),
        "unit_price": product["price"],
        "discount": float(discount_percent),
        "total": float(total_after),
    }
    sales_list.append(sale)
    return total_after


def total_sales(sales_list: List) -> float:
    """Return the sum of totals from the sales list."""
    return sum(s.get("total", 0.0) for s in sales_list)
