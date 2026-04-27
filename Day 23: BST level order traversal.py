import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        if root is None:
            return
        
        # Initialize the queue with the root node
        queue = [root]
        
        while queue:
            # Pop the first node from the queue (FIFO)
            current = queue.pop(0)
            
            # Print the current node's data
            print(current.data, end=" ")
            
            # Add left and right children to the queue for later processing
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        #Write your code here

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
