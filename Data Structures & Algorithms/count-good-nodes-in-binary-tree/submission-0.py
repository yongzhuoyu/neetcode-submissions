# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        #Create a helper to return the num of good nodes in this subtree
        #given the max value seen on this path before reaching this node 
        def dfs(node, max_so_far):
            #write the base case 
            if node is None:
                return 0
            #Count the current node if its value is greater than or equal to max_so_far
            if node.val >= max_so_far:
                current_count = 1 
            else:
                current_count = 0
            #Update the path maximum 
            new_max = max(node.val, max_so_far)
            #Recursively call the left and right subtree 
            left_count = dfs(node.left, new_max)
            right_count = dfs(node.right, new_max)
            
            return left_count + right_count + current_count
        return dfs(root, root.val)