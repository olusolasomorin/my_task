# Contact quick lookup
# Store three names and their phone numbers in two separate tuples.
# Ask the user for a name and display the corresponding number (or an error message).

name = ('Ayo', 'Seyi', 'Bolu')
phone_number = ('09130411877', '08100112233', '09012345678')
contact_info = dict(zip(name, phone_number))

name = input("Enter a name to search for their phone number: ")
print(contact_info.get(name, "No name in data base"))
