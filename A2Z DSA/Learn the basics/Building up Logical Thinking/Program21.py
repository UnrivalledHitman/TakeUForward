# Program to print a hollow square pattern
# Name = Indrajeet Mondal; Date = 27th July 2024
# SourceCode

x = int(input("Enter side length of the square pattern:- "))

# Outer loop for height of the pattern
for i in range(x):
    # Inner loop for row content
    for j in range(x):
        # Printing star condition
        if i == 0 or i == x - 1 or j == 0 or j == x - 1:
            print("* ", end="")
        # Printing space condition
        else:
            print("  ", end="")
    print()
