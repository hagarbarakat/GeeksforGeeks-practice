class Solution:
    # Your task is to Complete this function
    # function should return an integer
    def maxDistance(self, arr, n):
        hashmap = {}
        max_val = float("-inf")
        for i in range(n): 
            hashmap[arr[i]] = i 
        for i in range(n): 
            max_val = max(max_val, abs(hashmap[arr[i]] - i))
        return max_val