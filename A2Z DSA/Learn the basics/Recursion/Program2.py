# Print name N times using recursion
# Name = Indrajeet Mondal; Date = 3rd August 2024
# SourceCode


def print_name(name, times):
    if times > 0:
        print(f"{name}")
        print_name(name, times - 1)


x = input("Enter your name:- ")
y = int(input("Enter the number of times the name is to be printed:- "))

print_name(x, y)
