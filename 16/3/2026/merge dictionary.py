
colors = {"red", "green", "blue", "yellow"}


search_item = "green"


if search_item in colors:
    print(f"Yes, '{search_item}' is in the set.")
else:
    print(f"No, '{search_item}' is not there.")


if "purple" not in colors:
    print("Purple is missing from the collection.")