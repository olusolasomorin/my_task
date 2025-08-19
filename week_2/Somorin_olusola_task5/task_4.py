# Tuple Unpacking
# Ask a user for their:
# first name
# age
# favorite color
# home town
# store them in a tuple profile and unpack into variables.
# Print and use escape sequence to align each piece of information nicely.
print('\tEnter the following informations below')
first_name = input('First name: ')
age = input('Age: ')
favorite_color = input('Favourite color: ')
home_town = input('Home town: ')
user_info = tuple([first_name, age, favorite_color, home_town])
first_name, age, favorite_color, home_town = user_info
print(f'{first_name}\n{age}\n{favorite_color}\n{home_town}')