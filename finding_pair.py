"""
two pointer approch
"""

def is_pair(arr:list,x):
    start = 0
    end = len(arr)-1


    while start<end:
        if arr[start] + arr[end] == x:
            return arr[start],arr[end]
        elif arr[start] + arr[end] > x:
            end-=1
        else:
            start+=1

    return -1

arr = [2,5,8,12,30]
x = 14
print(is_pair(arr,x))
