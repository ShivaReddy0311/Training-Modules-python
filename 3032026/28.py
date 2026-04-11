import re
text = "i like python"
result = re.sub(r"(\ )","_",text)
print(result)
