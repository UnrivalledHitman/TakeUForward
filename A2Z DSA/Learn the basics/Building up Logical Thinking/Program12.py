# Program to print crown pattern with numbers
# Name = Indrajeet Mondal; Date = 21st July 2024
# SourceCode

x = int(input("Enter the height of the crown:- "))
# Count of spaces
y = 2 * (x - 1)

# Outer loop for height of the crown
for var1 in range(1, x + 1):
    # Printing numbers
    for var2 in range(1, var1 + 1):
        print(var2, end="")
    # Printing spaces
    for var3 in range(y):
        print(" ", end="")
    # Printing numbers in reverse
    for var2 in range(var1, 0, -1):
        print(var2, end="")
    # Maintaining the number of spaces at each row
    y -= 2
    print()
