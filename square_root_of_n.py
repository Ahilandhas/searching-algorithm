


"""
naive
"""


def square_root(n:int) -> int:
    for i in range(1,(n//2)+1):
        if i * i == n :
            return i

        elif i * i > n:
            return i-1

print(square_root(9))

"""
naive
"""

def square_root(n:int) -> int:
    i = 1
    while i * i <= n:
        i+=1

    return i-1

print(square_root(9))


"""
using binary search
"""

def square_root(n:int) -> int:
       low = 0
       high = n
       ans = -1

       while low <= high:
           mid = (low+high) // 2

           if mid * mid == n:
               return mid
           elif mid * mid > n:
               high = mid - 1

           else:
               low = mid+1
               ans = mid
       return ans


print(square_root(24))
