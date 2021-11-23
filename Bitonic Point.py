class Solution:
	def findMaximum(self,arr, n):
		start, end = 1, n - 2
		while start <=  end: 
		    mid = (start + end) // 2
		    if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]: 
		        return arr[mid]
		    elif arr[mid] < arr [mid + 1]:
		        start = mid + 1
		    else:
		        end = mid - 1
		        
		return arr[n-1]