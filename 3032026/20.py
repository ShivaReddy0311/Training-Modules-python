import re
text =input("enter name")
print(re.findall(r"[^a,e,i,o,u]",text))
