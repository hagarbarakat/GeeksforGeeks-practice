class Solution:
    def firstRepeated(self,arr, n):
        hashmap = {} 
        index = 0
        for i in range(n):
            if arr[i] in hashmap: 
                hashmap[arr[i]] += 1
            else: 
                hashmap[arr[i]] = 1
                
        for i in range(n): 
            if hashmap[arr[i]] > 1: 
                index += 1
                return index
            index += 1
        return -1 