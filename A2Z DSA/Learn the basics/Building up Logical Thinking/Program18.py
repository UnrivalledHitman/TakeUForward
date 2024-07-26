# Program to print pyramid with capital letters in reverse order depending on the row number
# Name = Indrajeet Mondal; Date = 26th July 2024
# SourceCode

x = int(input("Enter height of the pyramid:- "))

# Outer loop for the height of the pyramid
for i in range(x):
    # Inner loop for printing rows
    print_char = ord("A")
    for ch in range(print_char + x - i - 1, print_char + x):
        print(chr(ch), end=" ")
    print()
