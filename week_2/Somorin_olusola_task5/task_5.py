# Modify Tuple indirectly 
# Ask a user to enter three items for their shopping list.
# Store in a tuple shopping_list.
# Convert it to a list, then ask for two or more items to add.
# Convert back to a tuple and print the updated list using join() to display items separated by "|".
print('\tEnter 3 shopping list below:')
list1 = input('1. ')
list2 = input('2. ')
list3 = input('3. ')
shopping_list = tuple([list1, list2, list3])
shopping_list = list(shopping_list)
list4 = input('Enter 2 more items you want to buy\n4. ')
list5 = input('5. ')
shopping_list.append(list4)
shopping_list.append(list5)
shopping_list = tuple(shopping_list)
print('|'.join(shopping_list))