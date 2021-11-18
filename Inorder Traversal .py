'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing the inorder traversal of the tree. 
class Solution:
    
    def InOrder(self,root):
        inorder = []
        self.InorderTrav(root, inorder)
        return inorder
    
    def InorderTrav(self, root, inorder):
        if root: 
            self.InorderTrav(root.left, inorder)
            inorder.append(root.data)
            self.InorderTrav(root.right, inorder)