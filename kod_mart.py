"""
KOD Mart - Simple Cart and Discount System
---------------------------------------------
Features:
- Add items to cart
- Calculate total
- Apply a discount code (flat % or fixed amount)
- Display final amount

Run:
    python kod_mart.py
"""

from dataclasses import dataclass, field


# ---------- Data Models ----------

@dataclass
class Item:
    name: str
    price: float
    quantity: int = 1

    @property
    def subtotal(self) -> float:
        return round(self.price * self.quantity, 2)


@dataclass
class Cart:
    items: list = field(default_factory=list)

    def add_item(self, name: str, price: float, quantity: int = 1):
        if not name or not name.strip():
            raise ValueError("Item name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity <= 0:
            raise ValueError("Quantity must be at least 1.")
        self.items.append(Item(name.strip(), price, quantity))

    def get_total(self) -> float:
        return round(sum(item.subtotal for item in self.items), 2)

    def is_empty(self) -> bool:
        return len(self.items) == 0


# ---------- Discount Logic ----------

# Example discount codes. "percent" codes take a % off; "fixed" codes take a flat amount off.
DISCOUNT_CODES = {
    "SAVE10": {"type": "percent", "value": 10},
    "SAVE20": {"type": "percent", "value": 20},
    "FLAT50": {"type": "fixed", "value": 50},
    "WELCOME100": {"type": "fixed", "value": 100},
}


def apply_discount(total: float, code: str):
    """
    Returns (final_amount, discount_amount, message)
    """
    code = code.strip().upper()

    if not code:
        return total, 0.0, "No discount code applied."

    if code not in DISCOUNT_CODES:
        return total, 0.0, f"Invalid discount code: '{code}'."

    discount = DISCOUNT_CODES[code]

    if discount["type"] == "percent":
        discount_amount = round(total * (discount["value"] / 100), 2)
    else:  # fixed
        discount_amount = discount["value"]

    # Discount can't exceed the total (no negative final amount)
    discount_amount = min(discount_amount, total)
    final_amount = round(total - discount_amount, 2)

    return final_amount, discount_amount, f"Discount code '{code}' applied successfully."


# ---------- Display Helpers ----------

def print_receipt(cart: Cart, discount_amount: float, final_amount: float, code: str = None):
    print("\n" + "=" * 40)
    print("            KOD MART RECEIPT")
    print("=" * 40)
    for item in cart.items:
        print(f"{item.name:<20} x{item.quantity:<3} ${item.subtotal:>8.2f}")
    print("-" * 40)
    print(f"{'Subtotal:':<25}${cart.get_total():>8.2f}")
    if code:
        print(f"{'Discount (' + code + '):':<25}-${discount_amount:>7.2f}")
    print(f"{'Final Amount:':<25}${final_amount:>8.2f}")
    print("=" * 40 + "\n")


# ---------- Interactive CLI ----------

def main():
    cart = Cart()
    print("Welcome to KOD Mart!")
    print("Available discount codes: SAVE10 (10% off), SAVE20 (20% off), FLAT50 ($50 off), WELCOME100 ($100 off)\n")

    while True:
        print("Menu: [1] Add item  [2] View cart total  [3] Checkout  [4] Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Item name: ").strip()
            if not name:
                print("Error: Item name cannot be empty.\n")
                continue

            try:
                price = float(input("Price: ").strip())
            except ValueError:
                print("Error: Price must be a number (e.g. 49.99).\n")
                continue

            qty_input = input("Quantity (default 1): ").strip()
            try:
                quantity = int(qty_input) if qty_input else 1
            except ValueError:
                print("Error: Quantity must be a whole number.\n")
                continue

            try:
                cart.add_item(name, price, quantity)
                print(f"Added: {name} x{quantity} @ ${price:.2f}\n")
            except ValueError as e:
                print(f"Error: {e}\n")

        elif choice == "2":
            if cart.is_empty():
                print("Cart is empty.\n")
            else:
                print(f"Current Total: ${cart.get_total():.2f}\n")

        elif choice == "3":
            if cart.is_empty():
                print("Cart is empty. Add items before checkout.\n")
                continue
            total = cart.get_total()

            while True:
                code = input("Enter discount code (or press Enter to skip): ").strip()
                final_amount, discount_amount, message = apply_discount(total, code)
                if code and code.upper() not in DISCOUNT_CODES:
                    print(message + " Try again or press Enter to skip.\n")
                    continue
                print(message)
                break

            print_receipt(cart, discount_amount, final_amount, code.upper() if code else None)
            break

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.\n")


if __name__ == "__main__":
    main()
