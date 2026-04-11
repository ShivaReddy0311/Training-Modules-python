#input username and password 
username = input("Enter username ")
password = input ("Enter password")

#check login 
if username == "admin":
    if password == "1234":
        print("login sucessful")
    else:
        print("incorrect password")
else:
    print("invalid username")
    