class Solution:
    def maxLen(self, n, arr):
        hashmap = {}
        s = 0 
        res = 0 
        for i in range(n): 
            s += arr[i]
            if s == 0:
                res = max(res, i + 1)
            else:
                if s in hashmap:
                    res = max(res, i - hashmap[s])
                else:
                    hashmap[s] = i 
        return res
            