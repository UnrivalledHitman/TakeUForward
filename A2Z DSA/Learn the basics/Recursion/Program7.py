# Reverse an array (used in built method rather than recursion)
# Name = Indrajeet Mondal; Date = 3rd August 2024
# SourceCode

arr_len = int(input("Enter the length of the input array: "))
arr = []

for i in range(arr_len):
    x = int(input("Enter a number: "))
    arr.append(x)

print(f"Original array is: {arr}")

arr.reverse()
print(f"Reversed array is: {arr}")
