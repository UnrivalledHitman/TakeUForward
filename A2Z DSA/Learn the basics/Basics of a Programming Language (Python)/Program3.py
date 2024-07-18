# Job eligibility check
# Name = Indrajeet Mondal; Date = 3rd July 2024
# SourceCode

age = int(input("Enter your age:- "))

if age < 18:
    print("You are not eligible for job.")
elif age < 54:
    print("You are eligible for job.")
elif age < 57:
    print("You are eligible, but retirement soon.")
else:
    print("You ain't eligible anymore, retirement time.")
