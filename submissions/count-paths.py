from functools import cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return _unique_paths((0, 0), m, n)


@cache
def _unique_paths(cell: tuple[int, int], m: int, n: int):
    if cell == (m - 1, n - 1):
        return 1

    count = 0
    if cell[0] + 1 < m:
        count += _unique_paths((cell[0] + 1, cell[1]), m, n)
    if cell[1] + 1 < n:
        count += _unique_paths((cell[0], cell[1] + 1), m, n)

    return count
