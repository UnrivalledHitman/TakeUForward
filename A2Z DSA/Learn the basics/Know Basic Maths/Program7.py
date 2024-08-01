# Calculate GCD of two numbers (Better Approach)
# Name = Indrajeet Mondal; Date = 1st August 2024
# SourceCode

x = int(input("Enter first number:- "))
y = int(input("Enter second number:- "))

min_of_two = min([x, y])

for i in range(min_of_two, 0, -1):
    if x % i == 0 and y % i == 0:
        gcd = i
        break

print(f"GCD of {x} and {y} is {gcd}.")
