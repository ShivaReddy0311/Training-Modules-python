
my_list = [1, 2, 2, 3, 4, 4, 5, 1]
print("Original list:", my_list)


unique_set = set(my_list)
print("Converted to set:", unique_set)


unique_list = list(unique_set)
print("Back to a list (duplicates removed):", unique_list)

