"""Inventory management functions.

Uses a simple dictionary as in-memory storage. Each product is stored as:
{ 'id': str, 'name': str, 'price': float, 'stock': int }
"""
from typing import Dict, List


def add_product(inventory: Dict, pid: str, name: str, price: float, stock: int):
    """Add a new product to inventory.

    Raises ValueError for invalid values or if product already exists.
    """
    if not pid:
        raise ValueError("Product ID required")
    if pid in inventory:
        raise ValueError("Product ID already exists")
    if price < 0 or stock < 0:
        raise ValueError("Price and stock must be non-negative")

    inventory[pid] = {
        "id": pid,
        "name": name,
        "price": float(price),
        "stock": int(stock),
    }
    return inventory[pid]


def update_stock(inventory: Dict, pid: str, delta: int):
    """Update stock for a product by `delta` (can be negative).

    Raises KeyError if product not found, ValueError if resulting stock negative.
    """
    if pid not in inventory:
        raise KeyError("Product not found")
    new_stock = inventory[pid]["stock"] + int(delta)
    if new_stock < 0:
        raise ValueError("Resulting stock cannot be negative")
    inventory[pid]["stock"] = new_stock
    return new_stock


def search_product(inventory: Dict, query: str) -> List[Dict]:
    """Search products by id or name (case-insensitive)."""
    q = str(query).lower()
    results = []
    for p in inventory.values():
        if q in p["id"].lower() or q in p["name"].lower():
            results.append(p.copy())
    return results


def display_inventory(inventory: Dict):
    """Prints the inventory to stdout in a readable format."""
    if not inventory:
        print("Inventory is empty.")
        return
    for p in inventory.values():
        print(f"{p['id']}: {p['name']} - Price: {p['price']:.2f}, Stock: {p['stock']}")
