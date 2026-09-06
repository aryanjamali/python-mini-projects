def main():
    cart = []

    while True:
        choose = input("""
=== SMART CART MANAGER ===
1. Add Item
2. View Cart & Total
3. Remove Item
4. Checkout & Exit

Choose an option (1-4): """)

        if choose not in ["1", "2", "3", "4"]:
            print("Please choose a valid option (1-4).")
            continue
        elif choose == "1":
            add_item(cart)
        elif choose == "2":
            cart_and_total(cart)
        elif choose == "3":
            remove_item(cart)
        elif choose == "4":
            checkout(cart)
            break


def add_item(cart):
    item_name = input("Enter item name: ").strip()
    if not item_name:
        print("Item name cannot be empty.")
        return
    item_name = item_name.title()

    while True:
        item_price = input("Enter item price: ").strip()
        try:
            item_price = float(item_price)
        except ValueError:
            print("Item price is not a valid number.")
            continue
        if item_price > 0:
            break
        print("Price must be a positive number.")

    while True:
        item_quantity = input("Enter item quantity: ").strip()
        try:
            item_quantity = int(item_quantity)
        except ValueError:
            print("Item quantity is not a valid number.")
            continue
        if item_quantity > 0:
            break
        print("Quantity must be a positive number.")

    cart.append({"name": item_name, "price": item_price, "quantity": item_quantity})
    print(f"{item_name} added to cart.")


def cart_and_total(cart):
    if not cart:
        print("Cart is empty.")
        return

    total = 0
    for item in cart:
        item_total = item["price"] * item["quantity"]
        print(f"{item['name']}: ${item['price']:.2f} x {item['quantity']} = ${item_total:.2f}")
        total += item_total
    print(f"Total: ${total:.2f}")


def remove_item(cart):
    if not cart:
        print("Cart is empty.")
        return

    item_name = input("Enter item name to remove: ").strip().title()
    for item in cart:
        if item["name"] == item_name:
            cart.remove(item)
            print(f"{item_name} removed from cart.")
            return
    print(f"{item_name} not found in cart.")


def checkout(cart):
    if not cart:
        print("Cart is empty. Nothing to checkout.")
        return

    total = sum(item["price"] * item["quantity"] for item in cart)
    if total >= 300:
        total = total * 90 / 100
        print("You got 10% off!")
    print(f"Total amount due: ${total:.2f}")
    print("Thank you for shopping with us!")
    cart.clear()


if __name__ == "__main__":
    main()