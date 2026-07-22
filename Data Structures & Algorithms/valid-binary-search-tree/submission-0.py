# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #create a helper to return whether the subtree rooted at node is valid 
        def helper(node, low, high):
            #empty subtree is valid since it does not violate BST constraint
            if node is None:
                return True
            #check whether the current node violates the range 
            if node.val <= low:
                return False
            if node.val >= high:
                return False
            #recursively check the left and right subtrees with updated bounds
            #everything in left subtree must be greater than low but lesser than node.val
            left_valid = helper(node.left, low, node.val)
            #everything in right subtree must be greater than node.val but smaller than high
            right_valid = helper(node.right, node.val, high)
            #both results must be valid for the BST to be valid
            return left_valid and right_valid
        #Call the helper on root with widest possible range 
        return helper(root, float("-inf"), float("inf"))

