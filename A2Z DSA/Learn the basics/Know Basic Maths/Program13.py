# Check if a number is prime or not (Optimal Approach)
# Name = Indrajeet Mondal; Date = 1st August 2024
# SourceCode

import math

x = int(input("Enter a number:- "))
sqrt_x = int(math.sqrt(x))
count = 0

for i in range(1, sqrt_x + 1):
    if x % i == 0:
        count += 1
        if x // i != i:
            count += 1

if count == 2:
    print(f"{x} is a prime number.")
else:
    print(f"{x} is not a prime number.")
