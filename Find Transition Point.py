def transitionPoint(arr, n):
    #Code here
    #binary search 
    start = 0 
    end = len(arr) - 1
    while start <= end: 
        mid = (start + end)// 2
        if arr[mid] == 1 and arr[mid - 1] == 0: 
            return mid
        else: 
            if arr[mid] == 0: 
                start = mid + 1 
            else: 
                end = mid - 1
    if arr[0] == 1:
        return 0 
    else:
        return -1
        