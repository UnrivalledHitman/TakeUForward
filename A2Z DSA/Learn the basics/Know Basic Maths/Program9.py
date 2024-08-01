# Check if a number is an Armstrong number or not
# Name = Indrajeet Mondal; Date = 1st August 2024
# SourceCode

x = int(input("Enter a number:- "))

y = x
z = x

digit_count = 0
sum_num = 0

# Calculating no. of digits
while y > 0:
    y = y // 10
    digit_count += 1

# Calculating the sum of digits raised to the power of number of digits
while z > 0:
    rem = z % 10
    sum_num += rem**digit_count
    z = z // 10

if sum_num == x:
    print(f"{x} is an armstrong number.")
else:
    print(f"{x} is not an armstrong number.")
