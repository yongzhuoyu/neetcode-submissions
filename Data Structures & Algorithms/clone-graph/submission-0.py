"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #hash map that stores original node -> copied node 
        copy_map = {}

        #helper returns the copid version of the entire graph starting from current 
        def clone(current):
            #Check if current is None 
            if current is None:
                return None
            #Check if current has been copied 
            if current in copy_map:
                return copy_map[current]
            
            #Create and store copy for unseen nodes 
            new_node = Node(current.val)
            copy_map[current] = new_node

            #Iterate through every current's neighbors 
            for neighbor in current.neighbors:
                #Call clone on the neigbor to either retrieve or create the neighbor's copy 
                copied_neighbor = clone(neighbor)
                #Add the copied neighbour to new_node.neighbors 
                new_node.neighbors.append(copied_neighbor)
            #return new_node to parent call
            return new_node
        return clone(node)
            