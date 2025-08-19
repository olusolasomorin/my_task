# Task5: Student score tracker
# Ask the user for 3 student names.
# For each student, ask for their score.
# store the results in two list (one for names, one for scores).
# print a formatted output showing Name-Score, aligned neatly.
print('\tEnter 3 students name below:')
stu_name1 = input('1. ')
stu_name2 = input('2. ')
stu_name3 = input('3. ')
name1_score = input(f'Enter {stu_name1} score: ')
name2_score = input(f'Enter {stu_name2} score: ')
name3_score = input(f'Emter {stu_name3} score: ')
len_1, len_2, len_3 = 40 - len(stu_name1), 40 - len(stu_name2), 40 - len(stu_name3)  # obtaing word length for final formatting
title = "Student score list"
print(f'{title:^40}\n1. {stu_name1} {name1_score:>{len_1}}\n2. {stu_name2} {name2_score:>{len_2}}\n3. {stu_name3} {name3_score:>{len_3}}')