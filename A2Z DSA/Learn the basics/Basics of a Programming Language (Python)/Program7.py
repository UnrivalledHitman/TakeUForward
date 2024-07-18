# Functions basics
# Name = Indrajeet Mondal; Date = 17th July 2024
# SourceCode


def comparisonOfTwo(a, b):
    if a > b:
        print(f"{a} is greater than {b}.")
    elif a == b:
        print(f"The two numbers are equal.")
    else:
        print(f"{a} is smaller than {b}.")


x = int(input("Enter a number:- "))
y = int(input("Enter another number:- "))

comparisonOfTwo(x, y)
