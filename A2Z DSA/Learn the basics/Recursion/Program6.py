# Calculate factorial of a number using recursion
# Name = Indrajeet Mondal; Date = 3rd August 2024
# SourceCode


def calc_fact(num):
    if num > 1:
        return num * calc_fact(num - 1)
    else:
        return 1


fact = int(input("Enter a number: "))

factorial = calc_fact(fact)

print(f"The factorial of {fact} is {factorial}.")
