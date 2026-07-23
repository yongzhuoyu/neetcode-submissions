# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #Create an empty value list to store the sorted values 
        values = []
        #Inorder traversal through node subtree in sorted order and append each node value to values
        def helper(node):
            #Base case returns because there is no node to process
            if node is None:
                return 
            #Traverse to the left subtree 
            helper(node.left)
            #at each node, append its value to values 
            values.append(node.val)
            #Traverse to the right subtree
            helper(node.right)
        #Call the helper on root 
        helper(root)
        #Return kth smallest value in values 
        return values[k-1]