

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
