# Task2: Shopping list manager
# Create an empty list.
# Ask the user to enter 3 shopping items (one by one).
# Add them to the list.
# Display the list as a single string, separated by commas.
print("\tShopping list\nList out 3 items you want to buy below: ")
input_list1 = input("1. ")
input_list2 = input("2. ")
input_list3 = input("3. ")
lists = (f"{input_list1}, {input_list2}, {input_list3}")
print(lists)