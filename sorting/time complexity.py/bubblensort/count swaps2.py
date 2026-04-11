def bubble_sort_count(arr):
    n=len(arr)
    swap_count=0
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap_count+=1
    return arr,swap_count
arr=[3,7,2,9,1]
sorted_arr,swaps=bubble_sort_count(arr)
print("sorted:",sorted_arr)
print("total swaps:",swaps)