class Solution:
    def getSingle(self,arr, n):
        xor = 0
        for i in range(n): 
            xor ^= arr[i]
        return xor