# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #Longest path between any two nodes 
        self.diameter = 0
        #Use a helper function to return height at each node 
        #Base case: height is 0 when the current node is None 
        def height(node):
            if node is None:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            #Check the path through a node which is left height + right height
            self.diameter = max(
                self.diameter,
                left_height + right_height
            )
            #Returned height to its parent uses only the longest branch 
            return 1 + max(left_height, right_height)
        
        height(root)
        return self.diameter