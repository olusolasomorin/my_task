# UNILAG Admission possibility checker
print("UNILAG Admission Possibility Checker".center(70, " "))
print("Welcome to Unilag admission possibility checker. Thank you for choosing UNILAG, a place where future leaders are made.")
candform = dict()
cand_name = input("Enter your fullname: ").title()
print(f"Welcome {cand_name}.")
age = int(input(f"How old are you {cand_name}: "))
utme_score = int(input("Enter your jamb score: "))
cand_choice = input("Is UNILAG your first choice of institution (Yes/No)?: ").title()
utme = input("Did you participate in UNILAG post-utme screening (Yes/No): ").title()
# Collecting o'level results
o_level = {"English", "Mathematics"}
print("Five(5) credit passes at one sitting in relevant O'level subjects, including English Language and Mathematics\n1. English Language\n2. Mathematics")
count = 3
while count <= 5:
    subject = input(f"{count}. ").title()
    if subject in o_level:
        print(f"{subject} already exist")
    else:
        o_level.add(subject)
        count += 1
o_level_list = list(o_level)

o_level_grade = []
for subject in o_level_list:
    grade = input(f"Enter grade for {subject}: ").upper()
    o_level_grade.append(grade)

o_level_grades = {names: grade for names, grade in zip(o_level, o_level_grade)}
print(o_level_grades)

if age >= 16 and utme_score >= 200 and cand_choice == "Yes" and utme == "Yes":
    for key in o_level_grades:
        result = o_level_grades[key] == "A" or o_level_grades[key] == "B" or o_level_grades[key] == "C"
        if result == False:
            break
    if result == True:
        print("Congratulations, You are eligible for a possible admission.")
    else:
        print("Thank you for participating but unfortunately, you are not eligible for admission.")
else:
    print("We appreciate your interest but unfortunately, you are not eligible for possible admission.")