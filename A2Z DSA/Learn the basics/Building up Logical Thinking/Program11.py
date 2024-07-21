# Program to print pyramid with only 0s and 1s
# Name = Indrajeet Mondal; Date = 21st July 2024
# SourceCode

x = int(input("Enter height of the pyramid:- "))

# Outer loop for no. of rows
for var1 in range(1, x + 1):
    # If it is an odd row
    if var1 % 2 != 0:
        for var2 in range(var1):
            # Start with 0
            if var2 % 2 != 0:
                print("0", end="")
            # Start with 1
            else:
                print("1", end="")
        print()
    # Even row
    else:
        for var2 in range(var1):
            # Start with 1
            if var2 % 2 != 0:
                print("1", end="")
            # Start with 0
            else:
                print("0", end="")
        print()
