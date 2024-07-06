# Nested lists and list methods
# Name = Indrajeet Mondal; Date = 6th July 2024
# SourceCode

array_2d = [[j + i * 3 + 1 for j in range(3)] for i in range(3)]
print(f"The 2d array is:- {array_2d}")

reqd_elmnt = array_2d[1][2]
print(f"The required element is:- {reqd_elmnt}")

array_2d[0][0] = 10
print(f"After changing the element in first row and first column to 10:- {array_2d}")

new_row = [7, 8, 9]
array_2d.append(new_row)
print(f"After inserting a new row:- {array_2d}")

flatten_list = [element for row in array_2d for element in row]
print(f"The flattened array is:- {flatten_list}")
