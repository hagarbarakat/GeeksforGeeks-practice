'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''
class Solution:
    def display(self,node):
        print(node.data, end = " ")
        if node.next: 
            self.display(node.next)
# ----------------------------------------
'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''
class Solution:
    def display(self,node):
        while node: 
            print(node.data, end = " ")
            node = node.next