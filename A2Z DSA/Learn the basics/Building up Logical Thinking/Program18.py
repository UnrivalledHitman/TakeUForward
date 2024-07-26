# Program to print pyramid with capital letters in reverse order depending on the row number
# Name = Indrajeet Mondal; Date = 26th July 2024
# SourceCode

x = int(input("Enter height of the pyramid:- "))

# Outer loop for the height of the pyramid
for i in range(x):
    # Inner loop for printing rows
    for ch in range(ord("A") + x - 1 - i, ord("A") + x):
        print(chr(ch), end=" ")
    print()
