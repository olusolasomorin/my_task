# Simulate a football match ticket system
# Store all seat numbers (1 to 50) in a set.
# Ask users to "book" a seat by entering the number.
# Remove booked seats from the set
# Show remaining seats after booking
seat = set(range(1, 51))
print(f'Available seat number\n{seat}')
print('\tBook a seat from the available seat number')
seat_number = int(input('Choose a seat number: '))
print(f'You booked seat {seat_number}')
# removed = seat.remove(seat_number)
seat.remove(seat_number)
print(f'\tAvailable seat number(updated)\n{seat}')