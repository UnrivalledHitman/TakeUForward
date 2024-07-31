# Reverse the given number (Brute Force Approach)
# Name = Indrajeet Mondal; Date = 31st July 2024
# SourceCode

x = int(input("Enter a number:- "))
z = x
digits = []

# Extracting all the digits
while z > 0:
    y = z % 10
    digits.append(y)
    z = z // 10

reversed_num = 0

# Reversing the number
while len(digits) != 0:
    extracted_digit = digits.pop(0)
    place_value = extracted_digit * (10 ** (len(digits)))
    reversed_num += place_value

print(f"Reverse of {x} is {reversed_num}.")
