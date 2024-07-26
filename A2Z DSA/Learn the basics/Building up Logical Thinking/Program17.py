# Program to print pyramid with capital letters
# Name = Indrajeet Mondal; Date = 25th July 2024
# SourceCode

x = int(input("Enter height of the pyramid pattern:- "))

# Outer loop for the number of rows.
for i in range(x):
    # For printing the left side spaces.
    for j in range(x - i - 1):
        print(" ", end="")
    # For printing the characters.
    ch = "A"
    break_point = (2 * i + 1) // 2
    for j in range(1, 2 * i + 1 + 1):
        print(ch, end="")
        if j <= break_point:
            # ord() gives the unicode of the character passed as argument
            ch = chr(ord(ch) + 1)
        else:
            ch = chr(ord(ch) - 1)
    # for printing the right side spaces
    for j in range(x - i - 1):
        print(" ", end="")
    print()
