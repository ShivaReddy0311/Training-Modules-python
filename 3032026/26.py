import re
text = "apple,banana,orange,grapes"
result = re.split(r"[,]",text)
print(result)
