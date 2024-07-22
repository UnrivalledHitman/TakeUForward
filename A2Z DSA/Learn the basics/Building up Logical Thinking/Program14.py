# Program to print left aligned pyramid pattern with capital letters
# Name = Indrajeet Mondal; Date = 22nd July 2024
# SourceCode


# Function to convert number to character
def convert_to_char(a):
    return chr(a)


x = int(input("Enter height of the pyramid pattern:- "))

# Outer loop for no. of rows
for var1 in range(1, x + 1):
    # 65 is the ASCII code for 'A'
    y = 65
    # Inner loop printing the alphabets
    for var2 in range(var1):
        char = convert_to_char(y)
        print(f"{char} ", end="")
        y += 1
    print()
