def bubble_sort_count(arr):8 
    n = len(arr)

    swap_count = 0

    for i in range(n):
        for j in range (0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+i] = arr[j+i],arr[j]
                swap_count += 1

    return arr, swap_count 

arr = [4,3,2,1]
sorted_arr, swaps = bubble_sort_count(arr)
print("sorted:", sorted_arr)
print("total swaps:",swaps)