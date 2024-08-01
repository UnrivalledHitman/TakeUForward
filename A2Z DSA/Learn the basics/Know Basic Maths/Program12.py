# Check if a number is prime or not (Brute Force Approach)
# Name = Indrajeet Mondal; Date = 1st August 2024
# SourceCode

x = int(input("Enter a number:- "))
count = 0

for i in range(1, x + 1):
    if x % i == 0:
        count += 1

if count == 2:
    print(f"{x} is a prime number.")
else:
    print(f"{x} is not a prime number.")
