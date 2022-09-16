# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = None
        head = None
        carry = 0
        
        while l1 or l2 or carry:
            # Iterate over each value in the linked list
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0 
            # Add the two values (and any carried values)
            s = a + b + carry
            # If the result is greater than 10, carry a 1
            if s >= 10:
                s -= 10
                carry = 1
            else:
                carry = 0
            # Add the result to the new linked list
            if result:
                result.next = ListNode(s)
                result = result.next
            else:
                result = head = ListNode(s)
            # Move to the next nodes
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
                
            
        return head
        
