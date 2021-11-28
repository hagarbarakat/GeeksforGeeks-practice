class Solution:
    #Function to sort the array into a wave-like array.
    def convertToWave(self,arr,N):
        i = 0 
        j = 1 
        while j < N: 
            arr[i], arr[j] = arr[j], arr[i]
            i += 2
            j += 2