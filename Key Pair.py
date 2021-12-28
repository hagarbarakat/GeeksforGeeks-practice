class Solution:
    def hasArrayTwoCandidates(self, arr, n, x):
        hashset = set()
        for i in range(n):
            complement = x - arr[i]
            if complement in hashset:
                return True
            hashset.add(arr[i])
        return False
