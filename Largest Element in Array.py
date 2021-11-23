def largest(arr, n):  
    max_num = float('-inf')
    for i in range(n):
        if arr[i] > max_num: 
            max_num = arr[i]
    return max_num