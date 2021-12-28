from collections import Counter


class Solution:
    def topK(self, nums, k):
        hashmap = Counter(nums)
        arr = sorted(hashmap.items(), key=lambda x: (x[1], x[0]), reverse=True)
        return [x[0] for x in arr[:k]]
