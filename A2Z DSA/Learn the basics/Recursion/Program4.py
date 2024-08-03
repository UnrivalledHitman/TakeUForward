# Print N to 1 using recursion
# Name = Indrajeet Mondal; Date = 3rd August 2024
# SourceCode


def print_num(n, x):
    if n >= 1:
        print(n)
        print_num(n - 1, x)


num = int(input("Enter the number for which the recursion is to be performed:- "))

print_num(num, 1)
