# Understanding basic recursion
# Name = Indrajeet Mondal; Date = 3rd August 2024
# SourceCode


def recursion_msg_print(n):
    if n > 0:
        print("Hello World !!!")
        recursion_msg_print(n - 1)


x = int(input("How many times would you like to print 'Hello World !!!':- "))

recursion_msg_print(x)
