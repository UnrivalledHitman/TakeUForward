# Sum of first N natural numbers
# Name = Indrajeet Mondal; Date = 3rd August 2024
# SourceCode


def natural_num_sum(x, n):
    if x > n:
        return 0
    else:
        return x + natural_num_sum(x + 1, n)


last = int(input("Enter the number up to which cumulative sum is to be calculated: "))

cumulative_sum = natural_num_sum(1, last)

print(f"The sum of natural numbers upto {last} is {cumulative_sum}.")
