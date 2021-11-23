class Solution:
    def countZeroes(self, arr, n):
        start, end = 0, n - 1
        while start <= end: 
            mid = (start + end) // 2
            if arr[mid] == 0 and (mid == 0 or arr[mid - 1] == 1): 
                return n - mid
            elif arr[mid] == 1: 
                start = mid + 1
            elif arr[mid] == 0: 
                end = mid - 1
        return 0