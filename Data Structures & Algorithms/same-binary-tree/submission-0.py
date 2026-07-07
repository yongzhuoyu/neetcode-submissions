# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Returns whether the subtree rooted at p is identical to the subtree rooted at q 
        #3 types of base cases: 
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        #After confirming current node matches, check if children matches
        #Recursively calling the same function to check if both left and right subtree matches 
        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)
        #Return whether both recursive check on left and right branches are true 
        return left_same and right_same