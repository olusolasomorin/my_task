# Task6: Word analyzer
# Ask the user to input a word.
# print the lenght of the word.
# check if it is all uppercase, all lowercase, or title case.
# Reverse the word using slicing.
word = input('Enter word here: ')
print(len(word))
print(f'Uppercase: {word.isupper()}')
print(f'Lowercase: {word.islower()}')
print(f'Title case: {word.istitle()}')
print(word[::-1])