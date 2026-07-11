"""Utility helpers for Retail Sales Management System."""


def apply_discount(amount: float, percent: float) -> float:
    """Apply a percentage discount to amount.

    percent must be between 0 and 100 inclusive.
    """
    percent = float(percent)
    if percent < 0 or percent > 100:
        raise ValueError("Discount percent must be between 0 and 100")
    return amount * (1 - percent / 100.0)
