"""
naive approch
"""

def naiveSearch(arr, key):
    i = 0
    while True:
        if arr[i] == key:
            return i
        elif arr[i] > key:
            return -1
        i += 1

# Example
arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
key = 10
print(naiveSearch(arr, key))




#search in an indefinite sized arry


def binary_search(arr,target,start,end):
    while start <= end:
        mid = (start+end) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            start = mid+1

        else:
            end = mid -1

    return -1


def find_position(arr,target):
    start = 0
    end = 1

    while target > arr[end]:
        temp = end+1
        end = end + (end - start + 1) * 2
        start = temp
        print(start,end)

    return binary_search(arr,target,start,end)


arr = [1,10,200,300,400,500,600,700,800,900,1000,1100,1222,1333,13333,144444,1555555]
print(find_position(arr,600))
