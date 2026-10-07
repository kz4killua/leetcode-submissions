# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      _, max_diameter = dfs(root)
      return max_diameter
    

def dfs(node) -> tuple[int, int]:
    """Returns the height of the node and the diameter of that subtree."""
    if not node:
        return 0, 0

    l_height, l_diameter = dfs(node.left)
    r_height, r_diameter = dfs(node.right)

    height = 1 + max(l_height, r_height)

    diameter = max(
        l_height + r_height,
        l_diameter,
        r_diameter,    
    )

    return height, diameter
