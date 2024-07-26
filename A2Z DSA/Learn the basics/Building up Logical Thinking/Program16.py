# Program to print left aligned pyramid pattern with repetitive capital letters
# Name = Indrajeet Mondal; Date = 22nd July 2024
# SourceCode

x = int(input("Enter the height of the pyramid:- "))
# Declaring the character to be printed outside so that it changes only after each row
print_char = ord("A")

# Outer loop for height of the pyramid
for i in range(1, x + 1):
    # Inner loop for each row elements printing
    for j in range(i):
        print(chr(print_char), end="")
    print_char += 1
    print()
