# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # length = 0
        # curr = head 
        # #First pass: Count the nodes
        # while curr:
        #     length+=1
        #     curr = curr.next
        # target = length - n 
        # dummy = ListNode()
        # dummy.next = head 
        # pred = dummy
        # #Reach the targets predecessor
        # for i in range(target):
        #     pred = pred.next
        # pred.next = pred.next.next
        # return dummy.next

        #Create the a dummy node and attack it to head
        dummy = ListNode()
        dummy.next = head 
        #Create two pointer: slow and fast 
        slow = dummy
        fast = dummy
        #Move fast foward n times 
        for i in range(n):
            fast = fast.next
        #Move both pointers until fast reaches the final node 
        #Stop the while loop when fast in on the final node so slow is before the node to be removed 
        while fast.next:
            slow = slow.next
            fast = fast.next 
        #Slow is now tat the target's predecessor so we can delete slow.next 
        slow.next = slow.next.next
        return dummy.next