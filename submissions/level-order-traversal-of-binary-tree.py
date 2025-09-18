# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict

def _get_levels(root: TreeNode) -> dict[int, list[TreeNode]]:
    
    # Initialize data structures for a BFS
    seen = set()
    queue = deque()
    levels = defaultdict(list)

    queue.append((root, 0))
    levels[0].append(root.val)

    while queue:
        node, level = queue.popleft()
        if node not in seen:

            # Update the levels of the child nodes
            for child in (node.left, node.right):
                if child is not None:
                    levels[level + 1].append(child.val)
                    queue.append((child, level + 1))
            
            # Update the list of seen nodes
            seen.add(node)

    return levels

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        levels = _get_levels(root)
        # Note: Python dictionaries preserve insertion (e.g. level) order
        return list(levels.values())
