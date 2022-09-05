# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        n = 0
        node = head
        middle = head
        
        while node:
            # Move to the next node
            node = node.next
            n += 1
            # Move the middle node every two iterations
            if n % 2 == 0:
                middle = middle.next
                
        return middle
