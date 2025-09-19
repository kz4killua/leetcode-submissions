def get_neighbors(i, j, heights):
    """Yields the neighbors of a cell in all four directions."""
    rows, cols = len(heights), len(heights[0])
    for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_i = i + delta_i
        new_j = j + delta_j
        if (0 <= new_i < rows) and (0 <= new_j < cols):
            yield new_i, new_j

def dfs(
    i: int, 
    j: int, 
    heights: List, 
    seen: set,
):  
    """Save all cells that are reachable via DFS from (i, j)."""
    if (i, j) not in seen:
        seen.add((i, j))

        # Check all higher neighboring cells
        for new_i, new_j in get_neighbors(i, j, heights):
            if heights[i][j] <= heights[new_i][new_j]:
                dfs(new_i, new_j, heights, seen)

    return seen


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])
        indices = []
        for i in range(rows):
            for j in range(cols):
                indices.append((i, j))

        # Get all cells that flow to the Pacific
        pacific = set()
        for i, j in indices:
            if (i == 0) or (j == 0):
                dfs(i, j, heights, pacific)

        # Get all cells that flow to the Atlantic
        atlantic = set()
        for i, j in indices:
            if (i == (rows - 1)) or (j == (cols - 1)):
                dfs(i, j, heights, atlantic)
        
        return sorted(pacific & atlantic)
