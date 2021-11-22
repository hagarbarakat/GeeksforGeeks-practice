class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        arr.sort()
        for i in range(len(arr)): 
            left, right = i + 1, n -1 
            while left < right:
                s = arr[i] + arr[left] + arr[right]
                if s == 0: 
                    return True
                elif s < 0: 
                    left += 1
                else: 
                    right -= 1
        return False
        