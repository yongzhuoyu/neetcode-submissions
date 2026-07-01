"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #Map each original node to its copied node
        copies = {
            None: None
        }
        current = head
        while current:
            #Create a copy of the current node with the same value as original
            copies[current] = Node(current.val) 
            current = current.next
        #Connect the copied nodes to their copied next and random nodes using pointers
        current = head 
        while current:
            copied_node = copies[current]
            copied_node.next = copies[current.next]
            copied_node.random = copies[current.random]
            #Advance the current pointer
            current = current.next
        return copies[head]