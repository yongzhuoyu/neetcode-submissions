# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #Write a helper function to check whether the subtress of each node is balanced 
        #And return the height of the subtree 
        def check(node):
            if node is None:
                return True, 0
            left_balanced, left_height = check(node.left)
            right_balanced, right_height = check(node.right)
            #For the current node to be balanced, left and right subtree must be true
            #and their height should differ by no more than 1 
            if left_balanced and right_balanced and abs(left_height - right_height) <= 1:
                current_balanced = True
            else:
                current_balanced = False 
            #Calculate the height of the current node
            current_height = 1 + max(left_height, right_height)
            return current_balanced, current_height 
        #Call the helper on root 
        balanced, height = check(root)
        return balanced
