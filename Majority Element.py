class Solution:
    def majorityElement(self, arr, N):
        count = 1
        element = arr[0]
        for i in range(1,N): 
            if element == arr[i]: 
                count += 1
            else: 
                count -= 1
            if count == 0: 
                element = arr[i]
                count = 1
          
        count = 0 
        for i in range(N): 
            if arr[i] == element:
                count += 1
        if count > N/2: 
            return element
        return -1