# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # Get all numbers in the linked list
        numbers = ''
        while head:
            numbers += str(head.val)
            head = head.next
            
        # Check if the resulting string is a palindrome
        return numbers == numbers[::-1]
