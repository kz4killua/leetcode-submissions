# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Keep pointers to the head and tail of the merged lists
        head = None
        tail = None
        
        while list1 and list2:
            
            # Pick the next smallest node
            if list1.val <= list2.val:
                next = list1
                list1 = list1.next
            else:
                next = list2
                list2 = list2.next
            
            # Point the merged list to the next value
            if tail:
                tail.next = next
                tail = tail.next
            else:
                head = tail = next
    
    
        # Fill up with whatever is left in list1 or list2
        if tail:
            tail.next = list1 or list2
        else:
            head = tail = list1 or list2
            
        return head
