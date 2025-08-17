# Task4: Name organizer
# Ask the user to enter 5 names (separated by spaces).
# Convert all names to lowercase.
# Sort the list alphabetically.
# Display them one name per line. -Tips: use range(),sort(), for, in, split(), len(),lower()
namelist = input('Enter 5 names seperated by space: ')
namelist = namelist.lower()
spname = namelist.split()
stname = sorted(spname)
for name in stname:
    print(name)