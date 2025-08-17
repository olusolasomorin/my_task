# Unique members registration
# Ask the user to enter three names separated by commas.
# Convert them to a set to ensure uniqueness.
# Create a dictionary where each name is a key and its length is the value.
user_names = input("Enter three(3) names seperated by a comma: ").title().split(', ')
user_names = set(user_names) # convert to set to ensure uniqueness.
name_dict = {name: len(name) for name in user_names}
print(name_dict)