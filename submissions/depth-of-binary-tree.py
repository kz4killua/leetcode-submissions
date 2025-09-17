# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def _calculate_depth(node: TreeNode):
    if node is None:
        return 0
    return 1 + max(_calculate_depth(node.left), _calculate_depth(node.right))

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return _calculate_depth(root)
