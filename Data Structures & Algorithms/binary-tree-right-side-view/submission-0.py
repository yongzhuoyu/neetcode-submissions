# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #Check for Empty Tree 
        if root is None:
            return []
        #Initialise result and queue to store nodes to be processed
        result = []
        queue = deque()
        queue.append(root)
        #Process one level at a time if its not empty
        while queue:
            #Track the number of nodes to process in each level
            level_size = len(queue)
            #Store the last node in this level
            rightmost = None
            for i in range(level_size):
                #Remove node from queue, add its children to queue 
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                #Update the rightmost to the current node
                rightmost = curr
            #Add the rightmost val to result
            result.append(rightmost.val)
        return result