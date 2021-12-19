class Solution:
    def findPairs(self, arr, n):
        hashmap = {}
        for i in range(n):
            for j in range(i + 1, n):
                s = arr[i] + arr[j]
                t = (arr[i], arr[j])
                if s in hashmap:
                    return 1
                hashmap[s] = t
        return 0
