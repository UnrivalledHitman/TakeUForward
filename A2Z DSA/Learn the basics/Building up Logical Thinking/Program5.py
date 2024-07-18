# Program to print left aligned inverted pyramid
# Name = Indrajeet Mondal; Date 18th July 2024
# SourceCode

x = int(input("Enter the number of rows in the pyramid:- "))

for var1 in range(x, 0, -1):
    for var2 in range(var1):
        print("* ", end='')
    print()
