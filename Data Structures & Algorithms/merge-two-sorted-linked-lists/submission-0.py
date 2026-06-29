# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Dummy is a starting node that allows the next node to be attached to it 
        dummy = ListNode()
        tail = dummy 

        #Compare between the current nodes when both list have nodes 
        while list1 and list2:
            if list1.val <= list2.val:
                #connect the current list1 node after tail 
                tail.next = list1
                #Advace the list1 pointer to the next 
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            #Advance tail to the node just attached 
            tail = tail.next
        #Attach the remaining list that still contain nodes 
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        #Return the node after dummy
        return dummy.next