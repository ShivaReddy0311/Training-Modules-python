import re

text = "hello world"
result = re.findall("world$",text)

print(result)
