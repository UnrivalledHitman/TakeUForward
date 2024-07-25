# Program to print pyramid with capital letters
# Name = Indrajeet Mondal; Date = 25th July 2024
# SourceCode


# Function to convert number to character
def convert_to_char(a):
    return chr(a)


x = int(input("Enter height of the pyramid pattern:- "))

# Outer loop for height of the pyramid
for var1 in range(1, x + 1):
    # To print left side spaces
    for var2 in range(x - var1):
        print(" ", end="")
    # To print the capital letters
    # 65 is the ASCII code for 'A'
    y = 65
    # Increasing order of capital letters print
    for var3 in range((2 * var1 - 1)):
        print_char = convert_to_char(y)
        print(f"{print_char}", end="")
        y += 1
        z = y
    z -= 1
    # Decreasing order of capital letters print
    for var4 in range(2 * var1):
        print_char = convert_to_char(z)
        print(f"{print_char}", end="")
        z -= 1
    # To print the right side spaces
    for var5 in range(x - var1):
        print(" ", end="")
    print()
