# Count no. of digits in the given number (Brute-Force Approach)
# Name = Indrajeet Mondal; Date = 30th July 2024
# SourceCode

x = int(input("Enter a number:- "))
count = 0
z = x

while z > 0:
    z = z // 10
    count += 1

print(f"The number of digits in {x} is {count}.")
