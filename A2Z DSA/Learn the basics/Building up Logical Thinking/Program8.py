# Program to print a normal inverted pyramid
# Name = Indrajeet Mondal; Date = 20th July 2024
# SourceCode

x = int(input("Enter the number of rows in the pyramid:- "))

# Outer loop for height of the pyramid
for var1 in range(x):
    # Inner loop 1 to print left white spaces
    for var2 in range(var1):
        print(" ", end="")
    # Inner loop 2 to print the star
    for var3 in range(2 * x - (2 * var1 + 1)):
        print("*", end="")
    # Inner loop 3 to print the right white spaces
    for var4 in range(var1):
        print(" ", end="")
    print()
