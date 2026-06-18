# KOD_MART - SIMPLE CART & DISCOUNT SYSTEM 

A command-line shopping cart application that lets users add items, view the
running total, apply a discount code, and see the final amount due.

## Features

- Add items to a cart (name, price, quantity)
- View current cart total at any time
- Apply a discount code at checkout (percentage-based or flat amount)
- Display a final itemized receipt with subtotal, discount, and final amount
- Input validation with clear error messages (no crashes on bad input)

## Technology Stack

- **Language:** Python 3
- **Libraries:** Standard library only (`dataclasses`) — no external
  dependencies required
- **Interface:** Command-line (CLI), interactive text menu

## Project Structure

```
kod-mart/
├── kod_mart.py     # Application source code
└── README.md       # This file
```

## Setup and Run Instructions

### Prerequisites
- Python 3.7 or higher installed on your machine

Check your Python version:
```bash
python3 --version
```

### Running the App
1. Clone or download this repository.
2. Navigate to the project folder:
   ```bash
   cd kod-mart
   ```
3. Run the script:
   ```bash
   python3 kod_mart.py
   ```
   (On Windows, you may need to use `python kod_mart.py` instead.)

### Using the App
Once running, you'll see a menu:
```
Menu: [1] Add item  [2] View cart total  [3] Checkout  [4] Exit
```

- **Option 1 — Add item:** Enter item name, price, and quantity (quantity
  defaults to 1 if left blank).
- **Option 2 — View cart total:** Shows the running subtotal of all items
  currently in the cart.
- **Option 3 — Checkout:** Prompts for an optional discount code, then
  displays a full receipt with subtotal, discount applied, and final amount.
  This ends the session.
- **Option 4 — Exit:** Quits the app without checking out.

### Available Discount Codes (for testing)
| Code         | Type       | Value     |
|--------------|------------|-----------|
| SAVE10       | Percentage | 10% off   |
| SAVE20       | Percentage | 20% off   |
| FLAT50       | Fixed      | $50 off   |
| WELCOME100   | Fixed      | $100 off  |

Codes are case-insensitive (e.g. `save10` and `SAVE10` both work).

## Assumptions Made During Development

- **Single currency, no tax/shipping logic** — the app deals only with item
  prices, quantities, and a discount; tax and shipping are out of scope.
- **Discount codes are predefined** in a dictionary in the source code rather
  than pulled from a database or external file, since persistence was
  explicitly not required.
- **One discount code per checkout** — codes cannot be combined/stacked.
- **A fixed-amount discount cannot exceed the cart total** — the final amount
  is capped at $0 instead of going negative.
- **No cart persistence between runs** — the cart only exists for the
  duration of a single program session, per the stated requirements.
- **Checkout ends the session** — once a discount code is applied and the
  receipt is shown, the program exits rather than looping back to the main
  menu, since checkout represents the end of a shopping flow.
- **Quantity and price must be positive** — zero or negative values are
  rejected with a clear error message rather than silently accepted.

## Possible Future Enhancements
- Remove/edit items already in the cart
- Multiple discount codes or stacked discounts
- Persistent storage (file or database) for products/cart
- Unit test suite (e.g. with `pytest`)
