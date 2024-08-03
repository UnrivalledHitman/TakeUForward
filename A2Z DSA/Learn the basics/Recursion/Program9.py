# Print upto Nth Fibonacci number
# Name = Indrajeet Mondal; Date = 3rd August 2024
# SourceCode


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def print_fibonacci_series(n):
    print(f"The Fibonacci Series up to {n}th term:")
    for i in range(n + 1):
        print(fibonacci(i), end=" ")


n = int(input("Enter the value of n: "))
print_fibonacci_series(n)
