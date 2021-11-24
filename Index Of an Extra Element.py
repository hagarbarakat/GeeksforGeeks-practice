class Solution:
    def findExtra(self,a,b,n):
        start, end = 0 , n-1
        while start < end: 
            mid = (start + end)//2
            if a[mid] == b[mid]: 
                start = mid + 1
            else: 
                end = mid 
        return start