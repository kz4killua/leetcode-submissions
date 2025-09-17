# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def _invert_subtree(root: TreeNode):
    
    if root is None:
        return
    
    # Invert the left, then the right subtree
    _invert_subtree(root.left)
    _invert_subtree(root.right)

    # Swap the left and right children
    root.left, root.right = root.right, root.left

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        _invert_subtree(root)
        return root
        
