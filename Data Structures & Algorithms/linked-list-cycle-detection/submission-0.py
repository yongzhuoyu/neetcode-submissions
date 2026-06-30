# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Use two pointer moving at diff speed
        #slow moves one node at a time and fast moves two node at a time 
        #If there is no cycle, fast pointer will hit the end of the list
        #If there is a cycle, fast pointer will keep looping and end on the same node as slow 
        slow = head 
        fast = head 
        #Check if fast and fast.next is not None so fast can move two steps
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next 
            #Compare the node themselves not the value as different node might have the same value
            if fast == slow:
                return True
        return False