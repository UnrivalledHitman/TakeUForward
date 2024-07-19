# Program to print left aligned pyramid with repetitive numbers corresponding to the row number
# Name = Indrajeet Mondal; Date = 18th July 2024
# SourceCode

x = int(input("Enter the number of rows in the pyramid:- "))

# Outer loop for height of the pyramid
for var1 in range(1, x + 1):
    # Inner loop for rows
    for var2 in range(1, var1 + 1):
        print(var1, end="")
    print()
