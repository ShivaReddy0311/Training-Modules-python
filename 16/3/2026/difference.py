
set_a = {"Red", "Blue", "Green", "Yellow"}
set_b = {"Green", "Yellow", "Orange", "Purple"}


diff_1 = set_a - set_b


diff_2 = set_a.difference(set_b)

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Elements in A but not in B: {diff_1}")