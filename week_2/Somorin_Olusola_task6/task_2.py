# Unique name collector
# Write a program that collects the names of people attending a seminar (no duplicates allowed) and displays them in alphabetical order.
print('\tWrite out the names of people attending a seminar separated by a space')
names = input('')
names = names.split()
names = set(names)
names = list(names)
names.sort()
print(names)