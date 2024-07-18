# Printing rectangle pattern
# Name = Indrajeet Mondal; Date = 18th July 2024
# SourceCode

x = int(input("Enter the number of rows in the pattern:- "))
y = int(input("Enter the number of columns in the pattern:- "))

for var1 in range(x):
    for var2 in range(y):
        print("* ", end="")
    print()
