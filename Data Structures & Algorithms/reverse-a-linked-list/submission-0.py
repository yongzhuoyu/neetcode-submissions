# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #use two pointers to keep track of the previous node and the current node 
        previous = None 
        current = head

        #iterate through the list as long as current is not None 
        while current is not None:
            #store the next pointer first before updating it to previous 
            nxt = current.next
            #current to point at the previous node 
            current.next = previous
            #shift the previous to current 
            previous = current 
            #and shift the current to next 
            current = nxt 
        return previous 
