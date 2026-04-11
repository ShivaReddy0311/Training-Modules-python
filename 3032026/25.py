import re
text = "my number is 94901117676"
result = re.sub(r"\d","X",text)
print(result)
