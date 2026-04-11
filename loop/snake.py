snake = 1

while true:

    print("🐍" * snake)

    move = input("press enter to move snake or type exit:")

    if move == "exit":
        break
    snake += 1