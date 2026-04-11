import re
text = "ac abc abbc"
result = re.findall("ab+c",text)
print(result)
