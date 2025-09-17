# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def _is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]):
    if (p is None) and (q is None):
        return True
    if (p is None) != (q is None):
        return False

    if p.val != q.val:
        return False
    else:
        return (
            _is_same_tree(p.left, q.left) and _is_same_tree(p.right, q.right)
        )

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if _is_same_tree(root, subRoot):
            return True
        elif root is None:
            return False
        else:
            return (
                self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            )
