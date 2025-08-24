# Federal Government Scholarship Key Eligibility Requirements:
# Citizenship:
# Applicant must be a citizen of Nigeria. 
# Enrollment:
# Must be a registered, full-time undergraduate student in a recognized Nigerian university. 
# Other Scholarships:
# Applicants cannot be currently receiving any other scholarship from an entity in the Oil and Gas industry, whether national or international. 
# Academic Qualification:
# For undergraduate courses, applicants usually need five distinctions (As and Bs) in relevant subjects in their WAEC/WASSCE (May/June) exams, including English and Mathematics.

# My Thought Process
# Candidate must possess all the qualifications below else the candidate won't be able to fill the form completely which automatically makes the candidate not qualified for the scholarship but if the candidate successfully fills the form completely, that makes the candidate automatically qualified for the scholarship.
# Candidate must:
#1. Be a citizen of Nigerian
#2. Be enrolled in a recognised Nigerian university
#3. Not be enrolled in an ongoing scholarship
#4. Have at least 5 distinction in relevant subjects including English and Mathematics.
while True:
    print("FEDERAL GOVERNMENT SCHOLARSHIP ENROLLMENT FORM".center(70, " "))
    citizen = input("Are you a citizen of Nigeria (Yes/No): ").title()
    if citizen == "Yes":
        uni = input("Are you currently enrolled in a recognised Nigerian university (Yes/No): ").title()
        if uni == "Yes":
            scholarship = input("Are you currently enrolled in another scholarship (Yes/No): ").title()
            if scholarship == "No":
                academic_qual = input("Do you have have at least 5 distinctions(A's and B's) in relevant subjects including mathematics and English? (Yes/No): ").title()
                if academic_qual == "Yes":
                    eligibility = (citizen == "Yes") and (uni == "Yes") and (scholarship == "No") and (academic_qual == "Yes")
                    print(f"Eligibility: {eligibility}\nYou are eligible for this scholarship.")
                    break
                else:
                    print("Only candidate with at least 5 distinctions(A's and B's) in relevant subjects including mathematics and English are eligble.\nUnfortunately you are not eligible.\nTry again next year.")
            else:
                print("You can't proceed further because you are currently enrolled in a scholarship. Thanks for showing interest.")
        else:
            print("Your are not eligible for this scholarship. Thank you for reaching this stage.")
    else:
        print("Your are not eligible for this scholarship. Thank you for showing interest.")   