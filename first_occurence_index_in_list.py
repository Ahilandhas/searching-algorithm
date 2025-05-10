"""
naive approch

"""
def first_occurence(arr,n,x):
    for i in range(n):
        if arr[i] == x:
            return i

    return -1



arr = [5,10,10,15,15]
n = len(arr)
x = 15
print(first_occurence(arr,n,x))

"""
iterative binary search
"""


def first_occurence(arr,low,high,x):

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < x:
            low = mid+1

        elif arr[mid] > x:
            high = mid-1

        else:
            if arr[mid] == x and arr[mid-1] != x:
                return mid

            else:
                high = mid-1


arr = [5,10,10,15,15]
low = 0
high = len(arr)-1
x = 15
print(first_occurence(arr,low,high,x))


"""
Recursive binary search
"""


def first_occurence(arr,low,high,x):

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < x:
            return first_occurence(arr,mid+1,high,x)

        elif arr[mid] > x:
            return first_occurence(arr,low,mid-1,x)

        else:
            if arr[mid] == x and arr[mid-1] != x:
                return mid

            else:
                return first_occurence(arr,low,mid-1,x)


arr = [5,10,10,15,15]
low = 0
high = len(arr)-1
x = 10
print(first_occurence(arr,low,high,x))
