# Program to print pyramid with capital letters
# Name = Indrajeet Mondal; Date = 25th July 2024
# SourceCode

x = int(input("Enter height of the pyramid pattern:- "))

# Outer loop for the number of rows.
for i in range(x):
    # To print the left side spaces
    for j in range(x - i - 1):
        print(" ", end="")
    # To print characters
    print_char = ord("A")
    # Defining mid-point
    brk_pt = (2 * i + 1) // 2
    # Starting to print
    for k in range(1, 2 * i + 2):
        print(chr(print_char), end="")
        # Increasing till mid
        if k <= brk_pt:
            print_char += 1
        # Decreasing after mid
        else:
            print_char -= 1
    # To print the right side of spaces
    for l in range(x - i - 1):
        print(" ", end="")
    print()
