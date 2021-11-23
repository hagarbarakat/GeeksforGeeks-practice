class Solution:
	def countOddEven(self, arr, n):
		odd, even = 0, 0 
		for i in range(n): 
		    if arr[i] % 2 == 0: 
		        even += 1
		    else: 
		        odd += 1 
		print(odd, even)