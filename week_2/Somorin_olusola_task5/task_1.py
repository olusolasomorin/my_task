# Create and display
# Ask the user to enter three favourite Nigerian dishes (one at a time).
# Store them in a tuple called dishes.
# print the tuple in a single line, seperating items with commas.
# Use the \n escape sequence to print each dish on a new line.
print('\tEnter your 3 favourite Nigerian dishes below:')
dish1 = input('1. ')
dish2 = input('2. ')
dish3 = input('3. ')
dishes = (dish1, dish2, dish3)
print(dishes)
print(f'{dish1}\n{dish2}\n{dish3}')
