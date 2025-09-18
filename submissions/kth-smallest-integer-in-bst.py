# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def parse_bst(root: TreeNode, result: list) -> list[TreeNode]:
    """Convert the binary search tree into a sorted list."""
    if root.left:
        parse_bst(root.left, result)
    
    result.append(root.val)
    
    if root.right:
        parse_bst(root.right, result)    

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_values = []
        parse_bst(root, sorted_values)
        return sorted_values[k - 1]
