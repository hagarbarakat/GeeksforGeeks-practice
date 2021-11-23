class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        arr = []
        max_val = float('-inf')
        for num in reversed(A): 
            if num >= max_val:
                max_val = num 
                arr.append(max_val)
        return arr[::-1]