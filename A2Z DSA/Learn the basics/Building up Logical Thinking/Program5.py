# Program to print left aligned inverted pyramid
# Name = Indrajeet Mondal; Date 18th July 2024
# SourceCode

x = int(input("Enter the number of rows in the pyramid:- "))

# Outer loop for no. of rows
for var1 in range(x):
    # Inner loop for no. of columns
    for var2 in range(y):
        print("* ", end="")
    print()