text  = input("enter thr string:")

result = ""

for ch in text:
    if ch not in result:
        result += ch
    
print("string without duplicate:",result)