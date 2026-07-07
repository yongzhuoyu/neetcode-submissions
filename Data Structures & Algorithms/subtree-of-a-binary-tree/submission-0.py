# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #Helper function is used to compare exactly whether the subtree rooted at a 
        #is identical to the subtree rooted at b 
        def sameTree(a, b):
            #3 possible base cases
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False 
            if a.val != b.val:
                return False
            #Compare the left subtree and right subtree 
            left_same = sameTree(a.left, b.left)
            right_same = sameTree(a.right, b.right)

            return left_same and right_same
        
        #Main function is used to search whether subRoot appears anywhere inside root 
        if root is None:
            return False
        #Try using the current root and subRoot as the starting point
        if sameTree(root, subRoot):
            return True 
        #If not, search left subtree and right subtree for every possible starting point 
        left_contains_subtree = self.isSubtree(root.left, subRoot)
        right_contains_subtree = self.isSubtree(root.right, subRoot)
        #As long as subroot is found in one place, return True 
        return left_contains_subtree or right_contains_subtree

        
        