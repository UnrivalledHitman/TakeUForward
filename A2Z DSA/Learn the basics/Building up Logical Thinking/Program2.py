# Program to print left aligned pyramid
# Name = Indrajeet Mondal; Date = 18th July 2024
# SourceCode

x = int(input("Enter the height of the pyramid:- "))

for var1 in range(1, x+1):
    for var2 in range(var1):
        print("* ", end='')
    print()