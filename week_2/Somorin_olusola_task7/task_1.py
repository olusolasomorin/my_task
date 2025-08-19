# Student bio data storage
# Create a program that collects student bio-data from user input (name, age, gender, courses) and stores it in a dictionary.
# Courses should be stored as a list.
# Display the bio-data neatly using escape sequences.

# student bio-dat
name = input("Enter student's full name: ").title()
age = int(input("Enter student's age: "))
gender = input('Enter gender (male/female): ').capitalize()
course1 = input("Enter student's course:\n1. ").title()
course2 = input('2. ').title()
course3 = input('3. ').title()
course4 = input('4. ').title()
course5 = input('5. ').title()
courses =[course1, course2, course3, course4, course5]

# Student dictionary
student_bio = {
    'Student info':{
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Courses": courses
    }
}

# Output section
print("\n\t=== STUDENT BIO-DATA ===")
print(f"Name:\t\t{student_bio['Student info']["Name"]}")
print(f"Age:\t\t{student_bio['Student info']["Age"]}")
print(f"Gender:\t\t{student_bio['Student info']["Gender"]}")
print(f"Courses:\t{student_bio['Student info']['Courses']}")