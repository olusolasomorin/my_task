# Student Record
# Create an empty dictionary called student.
# Ask the user to input their name and age, then store them in the dictionary.
# Add a list of scores(e.g.,[70,85,90]) to the dictionary.
# Use a comparison operator to check if the student has passed (average score >= 50). Save the result (True/False) in the dictionary under the key "passed".
# Use a logical operator to check if the student is a teenager (age between 13 and 19). Save the result as "teenager". 
# Print out the complete record.

student = {}
student['Name'] = input("Enter student's name: ").title()
student['Age'] = int(input("Enter student's age: "))
student["Score"] = [89, 60, 90]
average_sum = sum(student["Score"])/len(student["Score"])
student["Passed"] = average_sum >= 50
student["Teenager"] = (student["Age"] >= 13) and (student["Age"] <= 19)
print("\n\t=== STUDENT RECORD ===")
print(f"Name: {student['Name']}")
print(f"Age: {student['Age']}")
print(f"Scores: {student["Score"]}")
print(f"Passed: {student["Passed"]}")
print(f"Teenager: {student["Teenager"]}")