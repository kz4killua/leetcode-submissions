# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        seen = set()

        # Follow all next pointers
        node = head
        while True:
            if node is None:
                return False

            if node in seen:
                return True
            else:
                seen.add(node)
                node = node.next
            
