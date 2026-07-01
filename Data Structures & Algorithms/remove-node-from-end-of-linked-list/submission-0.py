# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head 
        #First pass: Count the nodes
        while curr:
            length+=1
            curr = curr.next
        target = length - n 
        dummy = ListNode()
        dummy.next = head 
        pred = dummy
        #Reach the targets predecessor
        for i in range(target):
            pred = pred.next
        pred.next = pred.next.next
        return dummy.next