class Solution:
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,start,end):
        new_list = []
        result = 1
        for i in range(n): 
            new_list.append([start[i], end[i]])
        new_list.sort(key = lambda x : x[1])
        i = 0
        for j in range(1, n): 
            if new_list[j][0] > new_list[i][1]: 
                result += 1
                i = j
        return result