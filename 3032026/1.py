import re 
text = "my name is shiva reddy and i live in mancherial"
pattern = "mancherial"
result = re.search(pattern,text)
if result:
    print("match found")
else:
    print("matcgh not found")
