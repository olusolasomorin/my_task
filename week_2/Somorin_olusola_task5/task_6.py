# Attendance Tracker
# A python program that:
# Stores the days of the week in a tuple
# Stores the months of the year in another tuple.
# Ask user to enter their:
# Student's name
# Gender
# Course Track
# current month number(1-12)
# Current day number (1-7)
days_of_the_week = ('monday', 'tuseday', 'wednesday', 'thursday', 'friday')
# days_of_the_week_tuple = tuple(days_of_the_week)
# print(days_of_the_week)
months_of_the_year = ('january', 'february', ' march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')
# print(months_of_the_year)
print('\tEnter your details below')
stu_name = input('Student name: ')
gender = input('Gender: ')
course_track = input('Course track: ')
current_month = int(input('Current month number(1-12): '))
current_day = int(input('Current day number(1-7): '))
print(f"Student name: {stu_name}")
print(f"Gender: {gender}")
print(f"Course track: {course_track}")
print(f"Current month: {months_of_the_year[current_month -1]}")
print(f"Current day: {days_of_the_week[current_day -1]}")