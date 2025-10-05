# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Count the elements in the list
        count = 0
        
        node = head
        while node:
            count += 1
            node = node.next

        # Navigate to the item to be removed
        i = 0

        prev = None
        curr = head

        while i != (count - n):
            prev = curr
            curr = curr.next
            i += 1

        # Rewire links
        if prev:
            prev.next = curr.next
        else:
            head = curr.next

        return head
