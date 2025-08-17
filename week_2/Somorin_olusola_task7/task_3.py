# Days and activities pairing
# Store days of the week in a tuple and ask the user to input an activity for three specific days.
# Use dictionary comprehension to pair days and activities.
# Print the dictionary.

# Days of the week in a tuple
day_of_the_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print('Days of the week:', day_of_the_week)
# User selects 3 specific days
print('== Select three(3) specific days ==')
day1 = input('1. ').title()
day2 = input('2. ').title()
day3 = input('3. ').title()
selected_days = (day1, day2, day3)
# User input/output activities for the selected days
print('== Please enter an activity for the specific days ==')
activities = []
for day in selected_days:
    activity = input(f"Enter activity for {day}: ").title()
    activities.append(activity)
print('Your activites:', activities)

day_activity_dict = {day: activity for day, activity in zip(selected_days, activities)}
print("\n==== Day and Activity Pairing ====")
print(day_activity_dict)