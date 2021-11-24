class Solution:
    def subArraySum(self,arr, n, s): 
        k = 0
        i = 0
        current_sum = 0
        for i in range(n): 
            current_sum += arr[i]
            if current_sum == s: 
                return [k + 1, i+1]
            else: 
                while current_sum > s:
                    current_sum -= arr[k]
                    k += 1
                if current_sum == s: 
                    return [k + 1, i+1]
            
        return [-1]