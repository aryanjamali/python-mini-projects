# Smart Cart Manager

## Overview

Smart Cart Manager is a lightweight command-line shopping cart application built with Python. It allows users to add products, review cart contents, remove products, and complete a checkout with an automatic discount for orders of $300 or more.

## Key Features

- Add items with a name, price, and quantity
- Validate item names, prices, quantities, and menu choices
- View each cart item's subtotal and the current cart total
- Remove items by name
- Apply a 10% discount when the cart total is at least $300
- Display a checkout summary and clear the cart after checkout
- Runs using only the Python standard library

## How to Run

### Requirements

- Python 3.6 or later

### Steps

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the application:

```bash
python3 shopping-cart-cli.py
```

On Windows, use:

```bash
python shopping-cart-cli.py
```

### Available Menu Options

When the application starts, choose one of the following options:

1. **Add Item** - Enter a product name, price, and quantity.
2. **View Cart & Total** - Display all items and the current total.
3. **Remove Item** - Remove a product from the cart by name.
4. **Checkout & Exit** - Calculate the final amount, apply any discount, and exit.

## Concepts Used

- Functions for organizing application behavior
- Lists and dictionaries for storing cart data
- `while` loops for the interactive menu and input validation
- Conditional statements for menu routing and discount rules
- `try`/`except` for handling invalid numeric input
- String methods such as `.strip()` and `.title()` for input cleanup
- Generator expressions with `sum()` for calculating totals
- Formatted strings for currency and user-facing output
- The `if __name__ == "__main__"` entry-point pattern
