"""Retail Sales Management System - CLI

Very small, beginner-friendly command-line program for lab assessment.
"""
from inventory import add_product, update_stock, search_product, display_inventory
from sales import sell_product, total_sales


def main():
    inventory = {}
    sales = []

    menu = (
        "\nRetail Sales Management System\n"
        "1. Add product\n"
        "2. Update stock\n"
        "3. Search product\n"
        "4. Sell product / Apply discount\n"
        "5. Display inventory\n"
        "6. Calculate total sales\n"
        "7. Exit\n"
    )

    while True:
        try:
            choice = input(menu + "Choose an option: ").strip()
            if choice == "1":
                pid = input("Product ID: ").strip()
                name = input("Name: ").strip()
                price = float(input("Price: ").strip())
                stock = int(input("Stock: ").strip())
                add_product(inventory, pid, name, price, stock)
                print("Product added.")

            elif choice == "2":
                pid = input("Product ID: ").strip()
                delta = int(input("Stock change (use negative to reduce): ").strip())
                update_stock(inventory, pid, delta)
                print("Stock updated.")

            elif choice == "3":
                q = input("Search term (ID or name): ").strip()
                results = search_product(inventory, q)
                if results:
                    for p in results:
                        print(f"{p['id']}: {p['name']} - Price: {p['price']:.2f}, Stock: {p['stock']}")
                else:
                    print("No products found.")

            elif choice == "4":
                pid = input("Product ID: ").strip()
                qty = int(input("Quantity: ").strip())
                disc = float(input("Discount percent (0-100): ").strip())
                price_after = sell_product(inventory, sales, pid, qty, disc)
                print(f"Sold. Total: {price_after:.2f}")

            elif choice == "5":
                display_inventory(inventory)

            elif choice == "6":
                print(f"Total sales: {total_sales(sales):.2f}")

            elif choice == "7":
                print("Goodbye.")
                break

            else:
                print("Invalid option, try again.")

        except ValueError as e:
            print(f"Input error: {e}")
        except KeyError as e:
            print(f"Not found: {e}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
