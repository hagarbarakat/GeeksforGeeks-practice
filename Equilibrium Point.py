class Solution:
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        s = sum(A)
        s1 = 0
        for i in range(N): 
            if s - (s1 + A[i]) != s1: 
                s1 += A[i]
            else: 
                return i + 1
        return -1 