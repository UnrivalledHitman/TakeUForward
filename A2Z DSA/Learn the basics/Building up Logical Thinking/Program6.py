# Program to print inverted left aligned pyramid with numbers
# Name = Indrajeet Mondal; Date = 18th July 2024
# SourceCode

x = int(input("Enter the number of rows in the pyramid:- "))
for var1 in range(x, 0, -1):
    for var2 in range(1, var1 + 1):
        print(var2, end='')
    print()
