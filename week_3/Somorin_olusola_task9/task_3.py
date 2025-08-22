# Online store cart calculation
# Create a list of items (e.g., "Book", "Pen", "Bag") and another list of prices (e.g., 500, 100, 2000).
# Start with an empty cart total(cart_total = 0)
# Use assignment operators (+=) to add the price of some items into cart_total.
# Print the list of  items and the total price using an f-string

# List of items AND List of prices 
items = ["Bag", "Pencil", "Launch box", "Towel", "Air force"]
prices = [10000, 200, 3000, 6500, 35000]
cart_total = 0
add_items = []

print("\t=== Available items with price ===")
print("Items\t\tPrice")
print(f"{items[0]}\t\t#{prices[0]}")
print(f"{items[1]}\t\t#{prices[1]}")
print(f"{items[2]}\t#{prices[2]}")
print(f"{items[3]}\t\t#{prices[3]}")
print(f"{items[4]}\t#{prices[4]}")
print('\t=== Add items to your cart ===')
item1 = input(f"Do you want to add {items[0]} to your cart? (yes or no): ").title()
item2 = input(f"Do you want to add {items[1]} to your cart? (yes or no): ").title()
item3 = input(f"Do you want to add {items[2]} to your cart? (yes or no): ").title()
item4 = input(f"Do you want to add {items[3]} to your cart? (yes or no): ").title()
item5 = input(f"Do you want to add {items[4]} to your cart? (yes or no): ").title()
if item1 == ("Yes"):
    cart_total += prices[0]
    add_items.append(items[0])
    print(f"\nAdded {items[0]} to cart")
if item2 == ("Yes"):
    cart_total += prices[1]
    add_items.append(items[1])
    print(f"Added {items[1]} to cart")
if item3 == ("Yes"):
    cart_total += prices[2]
    add_items.append(items[2])
    print(f"Added {items[2]} to cart")
if item4 == ("Yes"):
    cart_total += prices[3]
    add_items.append(items[3])
    print(f"Added {items[3]} to cart")
if item5 == ("Yes"):
    cart_total += prices[4]
    add_items.append(items[4])
    print(f"Added {items[4]} to cart")
print("\n\t\t=== Cart summary ===")
print(f"Items in cart: {", ".join(add_items)}")
print(f"Total items: {len(add_items)}")
print(f"Total Price:", cart_total)