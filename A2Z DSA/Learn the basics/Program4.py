# Python lists basic operations
# Name = Indrajeet Mondal; Date = 6th July 2024
# SourceCode

my_list = []

for var in range(1, 11):
    my_list.append(var)

print(f"List with numbers from 1 to 10:- {my_list}")

my_list.append(11)

print(f"List after appending 11:- {my_list}")

my_list.remove(5)

print(f"List after removing 5:- {my_list}")

index = my_list.index(7)

print(f"The index of 7 is:- {index}")

print(f"Length of the list is:- {len(my_list)}")
