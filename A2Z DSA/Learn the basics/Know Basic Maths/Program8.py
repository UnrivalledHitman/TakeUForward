# Calculate GCD of two numbers (Optimal Approach using Euclidean Algorithm)
# Name = Indrajeet Mondal; Date = 1st August 2024
# SourceCode


def find_gcd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    if a == 0:
        return b
    return a


x = int(input("Enter first number:- "))
y = int(input("Enter second number:- "))

gcd = find_gcd(x, y)

print(f"GCD of {x} and {y} is {gcd}.")
