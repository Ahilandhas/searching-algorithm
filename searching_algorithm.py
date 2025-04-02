

def ord_seq_search(lst: list, ele):
    """"
    input should be sorted array
    """
    pos = 0
    stopped = False
    while pos < len(lst) and not stopped:
        if lst[pos] == ele:
            return f"element Found at index {pos}"

        else:
            if lst[pos] > ele:
                stopped = True

            else:
                pos += 1

    return "not found"


lst = [1, 2, 3, 5, 9, 15]
ele = 4

print(ord_seq_search(lst,ele))


def binary_search(lst: list, ele):
    """"
    input should be sorted array
    """
    start = 0
    end = len(lst)-1

    while start <= end:
        mid = (start + end) // 2

        if lst[mid] == ele:
            return mid

        elif lst[mid] < ele:
            start = mid+1

        else:
            end = mid -1

    return -1

lst = [1, 2, 3, 5, 9, 15]
ele = 9

print(binary_search(lst,ele))




def binary_search(L, start, end, item):
    if end >= start:
        middle = (start + end) // 2
        if L[middle] == item:
            return middle  # middle element is the item to be located
        # if middle item is greater than the item to be searched, left side of the list will be searched
        elif L[middle] > item:
            # starting index will be same but ending index will be the middle of the main list i.e. left half of the list is given in function.
            return binary_search(L, start, middle - 1, item)
        else:
            # if middle item is smaller than the item to be searched, new starting index will be middle of the list i.e. right half of the list.
            return binary_search(L, middle + 1, end, item)
    else:
        # if element is not present in the list
        return -1

    # Drivers code


my_list = [2, 4, 6, 9, 12, 16, 18, 19, 20, 21, 22]
element_to_search = 6
print("The given list is")
print(my_list)

index_of_element = binary_search(my_list, 0, len(my_list) - 1, element_to_search)

if index_of_element != -1:
    print("Element searched is found at the index ", str(index_of_element), "of given list")
else:
    print("Element searched is not found in the given list!")
