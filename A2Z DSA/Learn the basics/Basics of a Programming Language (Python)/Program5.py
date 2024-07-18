# Python list comprehensions and slicing
# Name = Indrajeet Mondal; Date = 6th July 2024
# SourceCode

original_list = [x for x in range(1, 21)]
print(f"The original list is:- {original_list}")

list_of_even_numbers = [var for var in original_list if var % 2 == 0]
print(f"The list of even numbers from 1 to 20:- {list_of_even_numbers}")

first_5_elmnts = original_list[0:5]
print(f"The first five elements of the original list is:- {first_5_elmnts}")

reversed_list = original_list[::-1]
print(f"The reversed list is:- {reversed_list}")
