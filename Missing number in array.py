class Solution:
    def MissingNumber(self,array,n):
        s = n*(n+1)//2
        for i in range(n - 1): 
            s -= array[i]
        return s 