class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        
        # Start with a list of all grid indices
        indices = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                indices.append((i, j))
        seen = set()

        for (i, j) in indices:
            
            if (i, j) in seen:
                continue

            seen.add((i, j))
            if grid[i][j] == '1':
                # Run a DFS to eliminate all connected lands
                eliminate_connected_components(grid, i, j, seen)
                count += 1

        return count

def eliminate_connected_components(
    grid: List[List[str]], i: int, j: int, seen: set
):

    # Explore all four directions: down, up, right, left
    for delta_i, delta_j in [
        (1, 0), (-1, 0), (0, 1), (0, -1),
    ]:
        new_i = i + delta_i
        new_j = j + delta_j
        
        # Ensure the new indices are within bounds
        if not (0 <= new_i < len(grid)):
            continue
        if not (0 <= new_j < len(grid[0])):
            continue

        # Ensure the new indices have not been seen
        if (new_i, new_j) in seen:
            continue
            
        seen.add((new_i, new_j))
        if grid[new_i][new_j] == '1':
            eliminate_connected_components(grid, new_i, new_j, seen)
        
