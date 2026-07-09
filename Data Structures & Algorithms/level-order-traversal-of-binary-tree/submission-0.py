# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Handle Empty Tree and the base case 
        if root is None:
            return []

        #Create a container to store final result 
        #and another to store nodes that are waiting to be processed 
        result = []
        queue = deque()
        queue.append(root)

        #Outer loop process one full level while there are nodes waiting in the queue 
        while queue:
            #Record the number of nodes currently at that level 
            level_size = len(queue)
            current_level = []
            #Process level_size number of nodes
            for i in range(level_size):
                #For each node, remove it from queue 
                curr = queue.popleft()
                #Add its value to the current_level 
                current_level.append(curr.val)

                #Add its children to queue for the next level
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            #Add the current_level to result 
            result.append(current_level)
        return result