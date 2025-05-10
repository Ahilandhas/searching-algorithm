"""
naive approch
"""



def count_1_in_binary_sorted_list(arr:list):
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == 0:
            return len(arr) - (i+1)


arr = [0,0,0,1,1,1,1]
print(count_1_in_binary_sorted_list(arr))

"""
using binary search approch
"""



def count_1_in_binary_sorted_list(arr,low,high,x):

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < x:
            low = mid+1

        elif arr[mid] > x:
            high = mid-1

        else:
            if arr[mid] == x and arr[mid-1] != x:
                return len(arr) - mid

            else:
                high = mid-1


arr = [0,0,0,1,1,1,1,1,1]
low = 0
high = len(arr)-1
x = 1
print(count_1_in_binary_sorted_list(arr,low,high,x))
