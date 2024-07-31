# Calculate GCD of two numbers (Brute Force Approach)
# Name = Indrajeet Mondal; Date = 31st July 2024
# SourceCode

x = int(input("Enter first number:- "))
y = int(input("Enter second number:- "))

x_divisors = []
y_divisors = []

# Calculating divisors of x
for i in range(1, x + 1):
    if x % i == 0:
        x_divisors.append(i)

# Calculating divisors of y
for j in range(1, x + 1):
    if y % j == 0:
        y_divisors.append(j)

# Calculating common divisors
common_divisors = set(x_divisors) & set(y_divisors)

# Calculating GCD
gcd = max(common_divisors)

print(f"GCD of {x} and {y} is {gcd}.")
