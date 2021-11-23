class Solution:
    def getPairsCount(self, arr, n, k):
        hashmap = {}
        count = 0 
        # hashmap with numbers and their freq 
        for i in range(n): 
            if arr[i] in hashmap: 
                hashmap[arr[i]] += 1
            else: 
                hashmap[arr[i]] = 1
            
        for i in range(n):
            complement = k - arr[i]
            if complement in hashmap:
                count += hashmap[complement]
                if complement == arr[i]: 
                    count -= 1

        return count//2