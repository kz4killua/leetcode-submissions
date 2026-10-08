class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        lo = 0
        hi = (m * n) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            mid_value = matrix_index(matrix, mid)

            if mid_value == target:
                return True
            elif mid_value > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return False


def matrix_index(matrix, i):
    n = len(matrix[0])
    r = i // n
    c = i % n
    return matrix[r][c]
