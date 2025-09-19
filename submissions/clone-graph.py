"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

def _deep_clone_graph(node: Node, seen: dict):

    if node.val in seen:
        return seen[node.val]
    
    # Clone the node itself (without neighbors)
    cloned_node = Node(val=node.val)
    seen[node.val] = cloned_node

    # Clone the node's neighbors
    cloned_neighbors = [
        _deep_clone_graph(n, seen) for n in node.neighbors
    ]
    cloned_node.neighbors = cloned_neighbors

    return cloned_node

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        seen = dict()
        return _deep_clone_graph(node, seen)
        
