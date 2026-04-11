import re
text = "my age is 21 years and i was born in 2004"
print(re.findall(r"[0-9]",text))
