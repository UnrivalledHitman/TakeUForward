# Count no. of digits in the given number (Optimal Approach)
# Name = Indrajeet Mondal; Date = 30th July 2024
# SourceCode

import math


def countDigits(n):
    # Calculate the number of digits in 'n' and casts it to an integer.
    cnt = int(math.log10(n) + 1)
    return cnt


x = int(input("Enter a number:- "))
count = countDigits(x)

print(f"{x} has {count} number of digits.")
