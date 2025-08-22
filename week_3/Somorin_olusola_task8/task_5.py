# Store inventory update 
# Create a dictionary called store with items and their available quantities. Example: store = {"Book": 10, "Pen": 20, "Bag": 5}
# Ask the user to input the item they want to buy (e,g., "Pen").
# Ask the user to input the quantity they want to purchase.
# Use the assignment operator -= to update (reduce) the item quantity in the dictionary.
# print the updated dictionary.
store =  {"Cross Bag": 20, "Pencil": 13, "Calculator": 15}
print("\t=== AVAILABLE ITEMS AND THEIR QUANTITY ===")
print(store)
user_buys = input("Enter the item you want to purchase: ").title()
user_buy_quant = int(input("Enter quantity: "))
store[user_buys] -= user_buy_quant
print("\t=== UPDATED ITEMS AND QUANTITY ===")
print(store)