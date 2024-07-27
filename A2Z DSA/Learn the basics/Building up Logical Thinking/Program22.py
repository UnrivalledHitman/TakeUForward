# Program to print square pattern with numbers decreasing by 1 till they reach the center
# Name = Indrajeet Mondal; Date = 27th July 2024
# SourceCode

x = int(input("Enter the square side length:- "))

# Outer loop for pattern height
for i in range(2 * x - 1):
    # Inner loop for pattern width
    for j in range(2 * x - 1):
        top = i
        bottom = j
        right = (2 * x - 2) - j
        left = (2 * x - 2) - i
        print(x - min(min(top, bottom), min(left, right)), end=" ")
    print()
