# Program to print half diamond pattern
# Name = Indrajeet Mondal; Date = 20th July 2024
# SourceCode

x = int(input("Enter half-height of the pattern:- "))
y = 1
z = 0

# Half diamond pattern base logic: left-aligned(normal pyramid + inverted pyramid) with some fine tuning
# First half of the diamond
while y <= x:
    for var in range(y):
        print("*", end="")
    print()
    y += 1

y -= 2

# Second half of the diamond
while z < y:
    for var in range(y):
        print("*", end="")
    print()
    y -= 1
