# Print 1 to N using recursion
# Name = Indrajeet Mondal; Date = 3rd August 2024
# SourceCode


def print_num(x, n):
    if n >= x:
        print(x)
        print_num(x + 1, n)


last_num = int(input("Enter the last number upto which the recursion is to be done:- "))

print_num(1, last_num)
