import re
text = "color,colour"
result = re.findall("colou?r",text)
print(result)
