import re
text = "akash is studiying engineering"
result = re.search("akash",text)
if result:
    print("match found")

