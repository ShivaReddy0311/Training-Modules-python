
keys = ["name", "age", "city"]
values = ["Leo", 25, "New York"]


user_dict = dict(zip(keys, values))

print(f"Keys: {keys}")
print(f"Values: {values}")
print(f"Resulting Dictionary: {user_dict}")

print(f"The user's name is: {user_dict['name']}")