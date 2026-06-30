# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Find the middle using slow and fast pointers 
        slow = head 
        fast = head 
        #after this, slow is at the middle index
        while fast.next and fast.next.next:
            fast = fast.next.next 
            slow = slow.next
        #Split the list by cutting the link from the middle 
        #Save slow.next into a variable before setting it None 
        second = slow.next
        slow.next = None
        #Reverse the second half
        prev = None 
        curr = second
        while curr:
            nxt = curr.next 
            curr.next = prev
            prev = curr
            curr = nxt
        #Merge the two list alternately
        second = prev
        first = head 
        while second:
            #Save next node from first 
            temp1 = first.next
            #Save next node from second 
            temp2 = second.next
            #Point first node to second node 
            first.next = second
            #Point second node to saved next first node 
            second.next = temp1 
            #Move both pointers foward 
            first = temp1
            second = temp2