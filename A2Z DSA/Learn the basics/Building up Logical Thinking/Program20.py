# Program to print two adjoint crows on the vertical axis pattern
# Name = Indrajeet Mondal; Date = 27th July 2024
# SourceCode

x = int(input("Enter height of the pattern:- "))

# Printing the top half
# Outer loop for no. of rows
for var1 in range(x):
    # Print the left side stars
    for var2 in range(var1 + 1):
        print("*", end="")
    # Print center spaces
    for var3 in range(2 * x - (2 * var1 + 1)):
        print(" ", end="")
    # Print the right side stars
    for var4 in range(var1 + 1):
        print("*", end="")
    print()

# Printing the lower half
# Outer loop for no. of rows
for var1 in range(x):
    # Print the left side stars
    for var2 in range(x - var1):
        print("*", end="")
    # Print center spaces
    for var3 in range(2 * var1 + 1):
        print(" ", end="")
    # Print the right side stars
    for var4 in range(x - var1):
        print("*", end="")
    print()
