# Grading System
# Name = Indrajeet Mondal; Date = 3rd July 2024
# SourceCode

marks = int(input("Enter your marks:- "))

if marks < 25:
    print("Your grade is F.")
elif marks <= 44:
    print("Your grade is E.")
elif marks <= 49:
    print("Your grade is D.")
elif marks <= 59:
    print("Your grade is C.")
elif marks <= 79:
    print("Your grade is B.")
else:
    print("Your grade is A.")
