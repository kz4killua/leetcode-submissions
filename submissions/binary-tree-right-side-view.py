from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        visible = dict()

        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if not node:
                continue

            visible[level] = node.val

            for child in [node.left, node.right]:
                queue.append((child, level + 1))

        # Python dicts now preserve insertion order, so this will return results ordered by level (from top to bottom).
        return list(visible.values())
