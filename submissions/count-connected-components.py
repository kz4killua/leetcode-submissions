from collections import defaultdict, deque


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # Build up neighbors from the adjacency list
        neighbors = defaultdict(set)
        for a, b in edges:
            neighbors[a].add(b)
            neighbors[b].add(a)

        output = 0
        
        unseen = set(range(n))

        # Run multiple breadth-first searches to get components
        while len(unseen) > 0:

            root = list(unseen)[0]
            queue = deque([(root, None)])
            
            while queue:
                node, parent = queue.popleft()

                if node in unseen:
                    unseen.remove(node)
                    for child in neighbors[node]:
                        if child != parent:
                            queue.append((child, node))

            # Update the number of connected components
            output += 1

        return output
