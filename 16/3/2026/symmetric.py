
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}


sym_diff_1 = set_a ^ set_b


sym_diff_2 = set_a.symmetric_difference(set_b)

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Symmetric Difference: {sym_diff_1}")
