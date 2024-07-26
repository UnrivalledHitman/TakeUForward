# Program to print inverted pyramid with capital letters
# Name = Indrajeet Mondal; Date = 22nd July 2024
# SourceCode

x = int(input("Enter height of the pyramid:- "))

# Outer loop for height of the pyramid
for i in range(x, 0, -1):
    # ASCII code for 'A'
    print_char = ord("A")
    # Printing row elements
    for j in range(i):
        print(chr(print_char), end="")
        print_char += 1
    print()
