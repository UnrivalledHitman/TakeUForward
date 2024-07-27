# Print hollow diamond within rectangle pattern
# Name = Indrajeet Mondal; Date = 27th July 2024
# SourceCode

x = int(input("Enter height of the pattern:- "))

# Printing the top half
# Outer loop for the number of rows
for var1 in range(x):
    # Inner loop 1 to print left side stars
    for var2 in range(x - var1):
        print("*", end="")
    # Inner loop 2 to print center spaces
    for var3 in range(2 * var1 + 1):
        print(" ", end="")
    # Inner loop 3 to print the right side stars
    for var4 in range(x - var1):
        print("*", end="")
    print()

# Printing the lower half
for var1 in range(x):
    # Inner loop 1 to print left side stars
    for var2 in range(var1 + 1):
        print("*", end="")
    # Inner loop 2 to print center spaces
    for var3 in range(2 * x - (2 * var1 + 1)):
        print(" ", end="")
    # Inner loop 3 to print the right side stars
    for var4 in range(var1 + 1):
        print("*", end="")
    print()
