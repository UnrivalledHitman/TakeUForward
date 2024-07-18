# Program to print left aligned pyramid with numbers from 1 to the number of row
# Name = Indrajeet Mondal; Date = 18th July 2024
# SourceCode

x = int(input("Enter the number of rows in the pyramid:- "))

for var1 in range(1, x + 1):
    for var2 in range(1, var1 + 1):
        print(var2, end="")
    print()
