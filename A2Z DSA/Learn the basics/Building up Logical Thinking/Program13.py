# Program to print pyramid with continuous numbers
# Name = Indrajeet Mondal; Date = 22nd July 2024
# SourceCode

x = int(input("Enter height of the pyramid:- "))
y = 1

# Outer loop for height of the pyramid
for var1 in range(1, x + 1):
    # Inner loop for no. of numbers in a row
    for var2 in range(var1):
        print(f"{y} ", end="")
        y += 1
    print()
