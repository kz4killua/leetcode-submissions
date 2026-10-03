import sys
# I could modify the DFS to use an iterative stack instead, but this is simpler.
sys.setrecursionlimit(50000)


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        visited = set()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X":
                    continue
                if (r, c) in visited:
                    continue

                region = {(r, c)}
                surrounded = dfs(board, r, c, region, True)

                if surrounded:
                    for nr, nc in region:
                        board[nr][nc] = "X"

                visited |= region


def dfs(board, r, c, region, surrounded):
    rows, cols = len(board), len(board[0])

    # If any of the 'O' cells is at an edge, update 'surrounded'
    if surrounded:
        if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
            surrounded = False

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

        if board[nr][nc] == "X":
            continue
        if (nr, nc) in region:
            continue

        region.add((nr, nc))
        if not dfs(board, nr, nc, region, surrounded):
            surrounded = False

    return surrounded
