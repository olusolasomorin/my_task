# Tuple and input
# Ask the user for 5 best friends' names.
# Store them in a tuple friends.
# Print the tuple in reverse order.
print("\nEnter your 5 best friends' name")
friend1 = input('1. ')
friend2 = input('2. ')
friend3 = input('3. ')
friend4 = input('4. ')
friend5 = input('5. ')
friend_list = (friend1, friend2, friend3, friend4, friend5)
print(friend_list[::-1])