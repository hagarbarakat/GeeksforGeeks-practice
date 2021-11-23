class Solution:
    def duplicates(self, arr, n): 
        res = []
        for i in range(n): 
            j = arr[i]%n
            arr[j] += n
        for i in range(n):
            if arr[i]//n > 1:
                res.append(i)
        if len(res) == 0:
            res.append(-1)
        return res