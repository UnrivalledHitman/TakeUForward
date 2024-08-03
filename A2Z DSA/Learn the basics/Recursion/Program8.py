# Check if a string is palindrome or not
# Name = Indrajeet Mondal; Date = 3rd August 2024
# SourceCode

x = input("Enter a string:- ")

if x == x[::-1]:
    print(f"{x} is a palindrome.")
else:
    print(f"{x} is not a palindrome.")
