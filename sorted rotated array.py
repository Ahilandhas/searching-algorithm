"""
search element in sorted rotated array
"""
def search_rotated_array(arr,target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [100,200,500,1000,2000,10,20]
target = 100

print(search_rotated_array(arr,target))

def search_rotated_array(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid

        # Check if left half is sorted
        if arr[start] <= arr[mid]:
            # Target lies in left half
            if arr[start] <= target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

        # Else, right half must be sorted
        else:
            # Target lies in right half
            if arr[mid] < target <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1

arr = [100,200,500,1000,2000,3000,3,10,20]
target = 3

print(search_rotated_array(arr,target))
