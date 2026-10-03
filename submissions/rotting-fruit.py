class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))

        result = 0

        seen = set()
        while len(queue) > 0:
            r, c, t = queue.popleft()

            # Turn fresh fruits rotten
            grid[r][c] = 2
            result = t

            for nr, nc in [
                (r + 1, c),
                (r - 1, c),
                (r, c + 1),
                (r, c - 1),
            ]:
                if not (0 <= nr < rows):
                    continue
                if not (0 <= nc < cols):
                    continue

                if (nr, nc) in seen:
                    continue
                else:
                    seen.add((nr, nc))

                if grid[nr][nc] == 1:
                    queue.append((nr, nc, t + 1))

        # Check if any fresh fruits are left
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return result
