# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def _validate_bst(root: TreeNode, lb: float, ub: float):
    # Check if the current level is valid
    if not (lb < root.val < ub):
        return False
    
    # Recursively check the child nodes
    if root.left:
        left_valid = _validate_bst(
            root.left,
            lb,
            root.val
        )
        if not left_valid:
            return False
    
    if root.right:
        right_valid = _validate_bst(
            root.right,
            root.val,
            ub
        )
        if not right_valid:
            return False
    
    return True

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        else:
            return _validate_bst(
                root, 
                float("-inf"),
                float("+inf"),
            )
