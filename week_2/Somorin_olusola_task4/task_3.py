# Task3: Word counter
# Ask the user for a sentence.
# Split the sentence into a list of words.
# Print how many words are in the sentence.
sentence = input("Write a sentence: ")
spl_sen = sentence.split()
print(spl_sen)
no_words = len(spl_sen)
print(no_words)