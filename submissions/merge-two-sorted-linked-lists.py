# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head, tail = None, None

        while True:
            if list1 is None and list2 is None:
                break
            
            # Pop the node to append to the result
            elif list1 is None and list2 is not None:
                node = list2
                list2 = list2.next
            elif list2 is None and list1 is not None:
                node = list1
                list1 = list1.next
            else:
                if list1.val <= list2.val:
                    node = list1
                    list1 = list1.next
                else:
                    node = list2
                    list2 = list2.next

            # Append the node to the result
            if head is None and tail is None:
                head = tail = node
                node.next = None
            else:
                tail.next = node
                tail = tail.next

        return head
