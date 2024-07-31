# Reverse the given number (Optimal Approach)
# Name = Indrajeet Mondal; Date = 31st July 2024
# SourceCode

x = int(input("Enter a number:- "))
z = x

# Extracting all the digits as well as printing in reverse order
while z > 0:
    if z % 10 == 0:
        z = z // 10
    else:
        print(z % 10, end="")
        z = z // 10
