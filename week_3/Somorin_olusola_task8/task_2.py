# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# score = int(input("Enter your test score: "))

# eligibility = (age < 18) and (score > 70)
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")
# """
# The code is a scholarship eligibility tacker for candidates that are below 18 years of age. It is used to check if a candidate is actually below the age of 18years and if they met the required score mark for the scholarship which is 70.
# """
print("\t==== FEDERAL GOVERNMENT SCHOLARSHIP ENROLLMENT FORM ====")
citizen = input("Are you a citizen of Nigeria (Yes/No): ").title()
uni_enrollment = input("Are you currently enrolled in a recognised Nigerian university (Yes/No): ").title()
scholarship = input("Are you currently enrolled in another scholarship (Yes/No): ").title()
academic_qual = input("Do you have have at least 5 distinctions(A's and B's) in relevant subjects including mathematics and English? (Yes/No): ").title()

eligibility = (citizen == "Yes") and (uni_enrollment == "Yes") and (scholarship == "No") and (academic_qual == "Yes")
print("Eligibility:", eligibility)