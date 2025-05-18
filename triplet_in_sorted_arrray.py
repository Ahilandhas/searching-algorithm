"""
Triplet in a sorted array
"""

"""
naive -> O(n*3)
"""

def is_triplet(arr:list,x:int):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if arr[i] + arr[j] + arr[k] == x:
                    return arr[i],arr[j],arr[k]



    else:
        return False


arr = [2,3,4,8,9,20,40]

arr = [1,2,5,6]
print(is_triplet(arr,8))


"""
using binary search -> O(n*2)
"""
def using_two_pointer(arr,start_index,target):
        start = start_index
        end = len(arr)-1

        while start<end:
            if arr[start] + arr[end] == target:
                return True
            elif arr[start] + arr[end] > target:
                end-=1
            else:
                start+=1

        return False

def is_triplet(arr:list,start,end,target:int):

    for i in range(len(arr)-2):
        if using_two_pointer(arr,i+1,target-arr[i]):
            return True
    return False
