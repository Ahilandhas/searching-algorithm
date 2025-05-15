"count occurence in a array"

def first_occurence(arr,n,x):
    low = 0
    high = n
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            if arr[mid] == x and arr[mid - 1] != x:
                return mid

            else:
                high = mid - 1


def last_occurence(lst,n,ele):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if lst[mid] < ele:
            start = mid + 1

        elif lst[mid] > ele:
            end = mid - 1

        else:
            if mid == len(lst) - 1 or lst[mid] != lst[mid + 1]:
                return mid
            else:
                start = mid + 1

    return -1

def find_occurence(arr,n,element):
    first = first_occurence(arr,n,element)
    if first == -1:
        return -1

    else:
        return last_occurence(arr,n,element) - first + 1

arr = [1, 2, 4, 8, 8,8, 8,8]
print(find_occurence(arr,len(arr)-1,8))
