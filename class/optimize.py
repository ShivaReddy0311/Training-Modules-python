def bubble_sort_optimized(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

    for i in range(n):
        for j in range (0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
                swapped = True

        if not swapped:
            break

    return arr, 

arr = [5,4,3,2,1]
print("optimized sorted:", bubble_sort_optimized(arr))