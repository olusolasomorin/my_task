# Super market price list
# Create a program that stores items and their prices in a dictionary.
# Items should come from a list.
# Prices are entered by the user.
# Display all items and prices, then allow the user to update the price of an item.
items = ['Bread', 'Rice', 'Beans', 'Nylon', 'Spoons']
print("==== SUPERMARKET PRICE LIST ===")
print("\nEnter price for each items in your local currency")
price_list = {}
for item in items:
    price_input = input(f"Enter price for {item}: #").strip()
    price = float(price_input)
    price_list[item] = price
print(price_list.items())

# To update price
print('Update your price list?')
for item in items:
    price_input = input(f"Enter price for {item}: #").strip()
    price = float(price_input)
    price_list[item] = price
price_list.update()
print(price_list)