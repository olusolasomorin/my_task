# Task7: List manipulation
# Create a list of five cities.
# Replace the third city with a new one (entered by the user)
# Remove the last city.
# Add a new city to the beginning of the list.
# Print the updated list.
five_cities = ['new york', 'New jersey', 'Washington', 'California', 'Atlanta']
print(five_cities)
new = input('Enter a new city: ')
five_cities[2] = new
print(five_cities)
five_cities.pop()
print(five_cities)
newcity = input('Enter a new city: ')
newcitylist = [newcity] + five_cities
print(newcitylist)