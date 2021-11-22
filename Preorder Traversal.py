'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
#Function to return a list containing the preorder traversal of the tree.
def preorder(root):
    arr = []
    preorder_trav(root, arr)
    return arr
       
def preorder_trav(root, arr): 
    if root:
        arr.append(root.data)
        preorder_trav(root.left, arr)
        preorder_trav(root.right, arr)