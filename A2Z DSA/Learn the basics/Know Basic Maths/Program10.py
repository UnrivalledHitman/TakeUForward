# Print all the divisors of the given number (Brute Force Approach)
# Name = Indrajeet Mondal; Date = 1st August 2024
# SourceCode

x = int(input("Enter a number:- "))
divisors = []

for i in range(1, x + 1):
    if x % i == 0:
        divisors.append(i)

for j in range(len(divisors)):
    print(divisors[j], end=" ")
