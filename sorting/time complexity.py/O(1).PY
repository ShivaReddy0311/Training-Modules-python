def constant_time(arr):
    print("\nO(1)-Constant Time Example")
    if len(arr)>0:
        print("First element:",arr[0])
    else:
        print("Array is empty")
arr=list(map(int,input("Enter elements separated")))
constant_time(arr)