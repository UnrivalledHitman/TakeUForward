# Print all the divisors of the given number (Optimal Approach)
# Name = Indrajeet Mondal; Date = 1st August 2024
# SourceCode

import math

x = int(input("Enter a number:- "))
divisors = []

sqrt_x = int(math.sqrt(x))

for i in range(1, sqrt_x + 1):
    if x % i == 0:
        divisors.append(i)
        if i != x // i:
            divisors.append(x // i)

divisors.sort()

for j in range(len(divisors)):
    print(divisors[j], end=" ")
