# Tuple Operations
# Create a tuple of 5 Nigerian states entered by the user.
# Print the first state and last state.
# Check if "Lagos" is in the tuple and print "yes" or "no".
# Print the number of states entered.
print('\tEnter 5 states in Nigeria')
state1 = input('1. ')
state2 = input('2. ')
state3 = input("3. ")
state4 = input('4. ')
state5 = input('5. ')
five_states = (state1, state2, state3, state4, state5)
print(five_states)
print((five_states[0], five_states[-1]))
if 'lagos' in five_states:
    print('lagos in tuple: Yes')
else:
    print('lagos in tuple: No')