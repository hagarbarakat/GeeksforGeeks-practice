class Solution:
    def reverseWords(self, S):
        s = S.split(".")
        return ".".join(reversed(s))
