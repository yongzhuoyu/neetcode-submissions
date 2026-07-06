# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Base case to stop the traversal: when current Node is None, return None 
        if root is None:
            return None
        #At each node, swap the child pointers 
        temp = root.left 
        root.left = root.right
        root.right = temp
        #Recursively invert both subtrees on the left and right
        self.invertTree(root.left)
        self.invertTree(root.right)
        #Return root 
        return root