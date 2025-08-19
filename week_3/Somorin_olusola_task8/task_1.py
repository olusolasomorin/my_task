# Explain each output of the program below.
# Give 3 usecases or scenarios where you can apply the program below.
# Write the code for 1 of the 3 use cases.
# num1 = int(input('Enter first number: '))
# num2 = int(input("Enter second number: "))
# print(f"{num1} == {num2} : {num1 == num2}")
#Explanation:
# The output gives true if both numbers inserted are equal.
# The output gves false if both numbers inserted are not equal.
# print(f"{num1} != {num2} : {num1 != num2}")
#Explanation:
# The output gives false if both number inserted are equal.
# The output gives true if both number inserted are nor equal.
# print(f"{num1} > {num2} : {num1 > num2}")
#Explanation:
# The output gives false if num1 is lesser/equal to num2
# The output gives true if and only if num1 is greather than num2.
# print(f"{num1} < {num2} : {num1 < num2}")
#Explanation:
# The output gives false if num1 is greather than/equal to num2
# The output gives true if and only if num1 is lesser than num2.

# Three usecases or scenarios
#1. Grade Comparison System - Compare student scores to determine pass/fail status, grade brackets, or ranking between students.
#2. Age Verification System - Compare user's age against minimum requirements for activities like voting, driving, or accessing age-restricted content.
#3. Temperature Monitoring System - Compare current temperature readings against safe operating ranges for equipment or comfort levels.

# Grade comparison system
print("\t==== GRADE COMPARISON SYSTEM ====")
print('This system compares two students score\n')
passed_mark = 60
student1 = int(input("Enter student1's score (0-100): "))
student2 = int(input("Enter student2's score (0-100): "))
print("\t==== Result comparison ====")
print(f"Student1 score: {student1}\tStudent2 score: {student2}")
print("Passed mark:", passed_mark)
print(f"\nStudent1 == Student2 : {student1 == student2}")
print(f"Student1 != Student2 : {student1 != student2}")
print(f"Student1 > Student2 : {student1 > student2}")
print(f"Student1 < Student2 : {student1 < student2}")
# Check if students met the passed mark
student1_status = student1 >= passed_mark
student2_status = student2 >= passed_mark
print("\n\t==== STUDENT STATUS ====")
print("Student1 Passed:", student1_status)
print("Student2 Passed:", student2_status)
print("Both students passed:", student1_status and student2_status)