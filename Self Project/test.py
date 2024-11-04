# Given list
code = [[1, 60], [2, 50], [3, 68]]

# Sorting the list based on the second value of each sublist
sorted_code = sorted(code, key=lambda x: x[1])

# Print the sorted list
print(sorted_code)
