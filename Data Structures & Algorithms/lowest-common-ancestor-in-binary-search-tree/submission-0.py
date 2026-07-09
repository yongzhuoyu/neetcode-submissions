# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #Starting from the root, return the LCA of p and q inside the subtree 
        #Case 1: both p and q are smaller than root, LCA must be in root.left 
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        #Case 2: both p and q are larger than root, LCA must be in root.right 
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        #Case 3: they split around root/one is root, so root is the LCA
        return root