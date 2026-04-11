import re
text = "I am 20 years old born in 2005 november"
print(("numbers"),(re.findall(r"\d",text)))
print(("words"),(re.findall(r"\w",text)))
print(("specific word"),(re.findall(r"years",text)))
       
