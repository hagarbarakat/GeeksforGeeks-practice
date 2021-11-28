class Solution:
	def removeDuplicates(self,str):
	    hashset = set()
	    res = ""
	    for ch in str: 
	        if ch not in hashset:
	            hashset.add(ch)
	            res += ch
	    return res
	       