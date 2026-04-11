import re
text = input("enter number")
result =re.fullmatch(r"\d{10}",text)
print("valid number")
    else:
        print("invalid number")
