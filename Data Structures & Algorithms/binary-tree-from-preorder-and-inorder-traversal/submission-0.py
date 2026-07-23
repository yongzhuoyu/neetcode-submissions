# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #Builds the subtree represented by preorder and inorder lists 
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #Base case: If there traversal list is empty, return None
        if not preorder:
            return None
        #Find the root of the current subtree and create a node using that value 
        root_value = preorder[0]
        node = TreeNode(root_value)
        #Find root index in inorder 
        root_index = inorder.index(root_value)
        left_size = root_index

        #Split inorder using root_index, left_inorder contains the left subtree and right_inorder contains the right subtree
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index + 1:]

        #Split preorder using left_size, left substree starts at index 1 
        #left_preorder takes left_size values and right_preorder takes right_size values 
        left_preorder = preorder[1: 1+left_size]
        right_preorder = preorder[1+left_size:]

        #Recursively build the left and right subtrees 
        node.left = self.buildTree(left_preorder, left_inorder)
        node.right = self.buildTree(right_preorder, right_inorder)

        return node