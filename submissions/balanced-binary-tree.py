# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _, is_balanced = dfs(root)
        return is_balanced


def dfs(node):
    if node == None:
        return 0, True

    l_height, l_is_balanced = dfs(node.left)
    r_height, r_is_balanced = dfs(node.right)

    height = 1 + max(l_height, r_height)

    is_balanced = l_is_balanced and r_is_balanced and abs(l_height - r_height) <= 1

    return height, is_balanced
