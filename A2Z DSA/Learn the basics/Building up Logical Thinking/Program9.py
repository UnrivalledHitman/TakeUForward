# Program to print diamond pattern
# Name = Indrajeet Mondal; Date = 20th July 2024
# SourceCode

x = int(input("Enter the half-height of the diamond pattern:- "))

# Loop 1:- for normal pyramid
for var1 in range(x):
    # Inner loop 1 to print left white spaces
    for var2 in range(x - var1 - 1):
        print(" ", end="")
    # Inner loop 2 to print the star
    for var3 in range(2 * var1 + 1):
        print("*", end="")
    # Inner loop 3 to print the right white spaces
    for var4 in range(x - var1 - 1):
        print(" ", end="")
    print()

# Loop 2: for normal inverted pyramid
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
