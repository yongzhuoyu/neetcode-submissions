# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy 
        carry = 0
        #Continue iterating if either list exists or carry = 1 
        while l1 or l2 or carry:
            #Read the current digit in both l1 and l2
            if l1:
                value1 = l1.val
            else:
                value1 = 0
            if l2:
                value2 = l2.val
            else:
                value2 = 0 
            #Calculate sum of value1 and value2, and compute the result digit and carry 
            total = value1 + value2 + carry
            digit = total % 10
            carry = total // 10 
            #Attach digit to tail and move tail pointer 
            tail.next = ListNode(digit)
            tail = tail.next 
            #Move both l1 and l2 foward if they exist 
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next 
        return dummy.next