
"""
using merge sort
"""

def median_of_two_sorted_array(arr1,arr2):
    i = 0
    j = 0
    arr = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1

    while i < len(arr1):
        arr.append(arr1[i])
        i+=1

    while j < len(arr2):
        arr.append(arr2[j])
        j+=1

    print(arr)

    if len(arr) % 2 == 0:
        mid = len(arr) // 2
        median = (arr[mid] + arr[mid-1]) / 2
        return median
    else:
        median = len(arr) // 2
        return arr[median]

arr1 = [10,20,30,40,50]
arr2 = [5,15,25,35,45   ]
print(median_of_two_sorted_array(arr1,arr2))
