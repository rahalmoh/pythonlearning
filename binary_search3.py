
#data = [5,6,8,99,43,53,23,111]
#target = 6

def binarySearch(data, target):

    low = 0
    high = len(data) -1

    while low <= high:
        mid = (low + high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
             low = mid +1
    
    return False

    
            