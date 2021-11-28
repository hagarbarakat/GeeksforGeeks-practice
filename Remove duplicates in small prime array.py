class Solution:
    def removeDuplicates(self, arr):
        dp = [0] * 100
    	tmp = list()
    	for prime in arr:
    		if dp[prime] == 0:
    			tmp.append(prime)
    			dp[prime] = 1
    	result = []
    	for prime in tmp:
    		result.append(prime)
    	return result
#----------------------------------------------
class Solution:
    def removeDuplicates(self, arr):
        hashset = set()
        res = []
        for i in range(len(arr)): 
            if arr[i] not in hashset: 
                hashset.add(arr[i])
                res.append(arr[i])
        return res