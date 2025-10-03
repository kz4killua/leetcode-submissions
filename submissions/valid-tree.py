from collections import defaultdict, deque


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # Construct the tree from the adjacency list
        neighbors = defaultdict(set)
        for a, b in edges:
            neighbors[a].add(b)
            neighbors[b].add(a)

        # Run a breadth-first search from any of the nodes
        seen = set()
        queue = deque([(0, None)])

        while queue:
            node, parent = queue.popleft()

            # If any cycles are found, the tree is invalid
            if node in seen:
                return False
            else:
                seen.add(node)
                for child in neighbors[node]:
                    if child != parent:
                        queue.append((child, node))

        # If any nodes are unreachable, the tree is invalid
        if len(seen) != n:
            return False

        return True
