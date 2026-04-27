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

    def getHeight(self,root):
        if root is None:
            return -1
        
        # Recursive Case: Get height of left and right subtrees
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        
        # Return 1 plus the maximum of the two subtree heights
        return max(left_height, right_height) + 1
        #Write your code here
        

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       
