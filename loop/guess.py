secret_number = 3
guess = 0 
while guess != secret_number:
    guess = int(input("enter yoyr guess: "))
    if guess == secret_number:
        print("correct ! you guesssed the number.")
    else:
        print("wrong guess. try again!")