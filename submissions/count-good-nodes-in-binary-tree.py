# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0

        def dfs(node: TreeNode, ub: float):
            nonlocal good_nodes

            if not (ub > node.val):
                good_nodes += 1

            ub = max(node.val, ub)
            for child in [node.left, node.right]:
                if child:
                    dfs(child, ub)

        dfs(root, float("-inf"))
        return good_nodes
