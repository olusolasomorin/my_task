#  Create a unique voters registration system
# Ask for voter names and store in a set.
# If a voter tries to register twice, display a warning.
# After registration, display the total number of uniques voters.
voters_name = set()
print('Voters registration system'.center(60, '-'))
name1 = input('Enter the voters name below\n1. ').title()
if name1 not in voters_name:
    voters_name.add(name1)
else:
    print(f'{name1} is a registered user')
name2 = input('2. ').title()    
if name2 not in voters_name:
    voters_name.add(name2)
else:
    print(f'{name2} is a registered user')
name3 = input('3. ').title()
if name3 not in voters_name:
    voters_name.add(name3)
else:
    print(f'{name3} is a registered user')
print(voters_name)    
print('Total number of registered user is:', len(voters_name))