

def index_of_last_occurence(arr: list, ele):
    """"
    input should be sorted array
    """
    index = None
    for i in range(len(arr)):
        if arr[i] == ele:
            index = i
    if index is not None :
        return index

    return -1


arr = [1,1,1, 2, 3, 5, 9,15, 15]
ele = 15

print(index_of_last_occurence(arr,ele))


def index_of_last_occurence(arr: list, ele):
    """"
    input should be sorted array
    """
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == ele:
            return i

    return -1


arr = [1,1,1, 2, 3, 5, 9,15, 15]
ele = 15

print(index_of_last_occurence(arr,ele))

"""
using binary search
"""

def last_occurence_with_binary_search(lst: list, ele):
    """"
    input should be sorted array

    """
    start = 0
    end = len(lst)-1
    index = None

    while start <= end:
        mid = (start + end) // 2

        if lst[mid] < ele:
            start = mid+1

        elif lst[mid] > ele:
            end = mid -1

        else:
            if mid == len(lst) -1 or lst[mid] != lst[mid+1]:
                return mid
            else:
                start = mid+1

    return -1

lst = [5,10,10,10,10,20,20]
ele = 10

print(last_occurence_with_binary_search(lst,ele))

