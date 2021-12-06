class Solution:
    def countBuildings(self,h, n):
        count, max_num = 1, h[0]
        for i in range(1, n):
            if h[i] > max_num: 
                count += 1
                max_num = h[i]
        return count