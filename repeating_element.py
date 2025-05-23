"""
repeating element
"""
"""
naive approch
"""
def repeating_element(arr:list):
    result = []
    for i in range(len(arr)):
        if arr[i] not in result:
            result.append(arr[i])
        else:
            return arr[i]

    return -1

arr = [0,2,1,3]
print(repeating_element(arr))

"""
using sort algorithm approch
"""
def repeating_element(arr:list):
   for i in range(len(arr)):
       for j in range(i+1,len(arr)):
           if arr[j] < arr[i]:
               arr[i],arr[j] = arr[j],arr[i]

   for i in range(len(arr)):
       if arr[i] == arr[i+1]:
           return arr[i]
   return -1


arr = [0,2,1,3,5,2,-1]
print(repeating_element(arr))

"""
using sort algorithm approch
"""
def repeating_element(arr:list):
   for i in range(len(arr)):
       for j in range(i+1,len(arr)):
           if arr[j] == arr[i]:
                return arr[i]

   return -1

arr = [0,2,1,3,5,2,-1]
print(repeating_element(arr))


"""
Time complexity O(n)
"""

def repeat_element(arr:list) -> int:
    visit = [False] * (len(arr)-1)
    for i in range(len(arr)):
        if visit[arr[i]]:
            return arr[i]

        visit[arr[i]] = True
    return -1

arr = [0,2,1,3,5,2,-1]
print(repeat_element(arr))

"""
Repeating element with O(1) and No changes to original array
"""

"""
Time complexity O(n)
space O(1)
"""

def repeat_element(arr:list) -> int:
    slow,fast = 0,0
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]

        if slow == fast:
            break
    slow2 = 0
    slow = 0

    while True:
        slow = arr[slow]
        slow2 = arr[slow2]

        if slow == slow2:
            return slow

arr = [2,1,3,5,2,-1]
print(repeat_element(arr))

"""
Repeating element with O(1) and No changes to original array
"""
