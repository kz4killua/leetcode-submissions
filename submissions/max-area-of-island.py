class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        # These are the 1's we've explored via DFS.
        seen = set()

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                if (r, c) in seen:
                    continue

                # At this point, we've discovered new land.
                area = dfs(grid, r, c, seen)
                max_area = max(max_area, area)

        return max_area


def dfs(grid, r, c, seen):
    rows, cols = len(grid), len(grid[0])

    if grid[r][c] != 1:
        return 0
    if (r, c) in seen:
        return 0
        
    seen.add((r, c))
    
    area = 1
    for nr, nc in [
        (r + 1, c),
        (r - 1, c),
        (r, c + 1),
        (r, c - 1),
    ]:
        # Ensure the neighbor is within bounds
        if not (0 <= nr < rows):
            continue
        if not (0 <= nc < cols):
            continue

        area += dfs(grid, nr, nc, seen)

    return area
