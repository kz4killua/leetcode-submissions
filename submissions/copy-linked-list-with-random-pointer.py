"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_node_indices = dict()
        new_node_indices = dict()

        # Store the index of each old (original) node
        i = 0
        node = head
        while node:
            old_node_indices[node] = i
            node = node.next
            i += 1

        # Store the index of each new (copied) node
        j = 0
        node = head
        while node:
            new_node = Node(node.val)
            new_node_indices[new_node] = j
            node = node.next
            j += 1

        # Assign random and next
        n = len(new_node_indices)
        new_node_objects = {v: k for k, v in new_node_indices.items()}
        old_node_objects = {v: k for k, v in old_node_indices.items()}

        for i in range(n):
            old_node = old_node_objects[i]
            new_node = new_node_objects[i]

            if old_node.next:
                index = old_node_indices[old_node.next]
                new_node.next = new_node_objects[index]

            if old_node.random:
                index = old_node_indices[old_node.random]
                new_node.random = new_node_objects[index]

        return new_node_objects[0]
