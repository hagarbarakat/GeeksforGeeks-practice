class Solution:
    def rearrange(self,arr, n):
        positive = []
        negative = []
        for i in range(n): 
            if arr[i] < 0: 
                negative.append(arr[i])
            else: 
                positive.append(arr[i])
        i,j,k = 0,0,0
        while i < len(positive) and j < len(negative):
            arr[k] = positive[i]
            k += 1
            arr[k] = negative[j]
            k += 1
            i += 1
            j += 1
        while i < len(positive): 
            arr[k] = positive[i]
            k += 1
            i += 1
        while j < len(negative): 
            arr[k] = negative[j]
            k += 1
            j += 1