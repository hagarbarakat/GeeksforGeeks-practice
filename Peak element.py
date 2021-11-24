class Solution:   
    def peakElement(self,arr, n):
        start, end= 0, n-1
        while start < end: 
            mid = start + (end - start) // 2
            if arr[mid] < arr[mid + 1]:
                start = mid + 1
            else:
                end = mid
        return start
       