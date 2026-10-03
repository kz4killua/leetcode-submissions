from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))

        seen = set()
        while len(queue) > 0:

            r, c, d = queue.popleft()

            if (r, c) in seen:
                continue
            else:
                seen.add((r, c))

            if grid[r][c] >= 1:
                grid[r][c] = min(grid[r][c], d)
            
            for nr, nc in [
                (r + 1, c),
                (r - 1, c),
                (r, c + 1),
                (r, c - 1),
            ]:
                # Ensure we remain within bounds
                if not (0 <= nr < rows):
                    continue
                if not (0 <= nc < cols):
                    continue

                if grid[nr][nc] <= 0:
                    continue

                queue.append((nr, nc, d + 1))
