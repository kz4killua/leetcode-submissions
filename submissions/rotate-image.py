class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        # Initialize the outermost edge of the matrix
        top, bottom, left, right = 0, n - 1, 0, n - 1

        rotate_recursively(n, matrix, top, bottom, left, right)


def rotate_recursively(n, matrix, top, bottom, left, right):
    """Recursively rotate a matrix from the outer to the inner cells."""

    if (top >= bottom or left >= right):
        return

    # Rotate the elements on the outer edges of the matrix
    row = top
    for col in range(left, right):

        temp = matrix[row][col]
        for i in range(4):
            new_row, new_col = get_rotated_index(row, col, n)
            new_temp = matrix[new_row][new_col]
            matrix[new_row][new_col] = temp
            row, col, temp = new_row, new_col, new_temp

    # Adjust the pointers to move to inner cells
    top += 1
    bottom -= 1
    left += 1
    right -= 1

    # Recursively rotate inner cells
    rotate_recursively(n, matrix, top, bottom, left, right)


def get_rotated_index(row, col, n):
    """Returns the new index of an item in the rotated n x n matrix."""
    return (col, n - 1 - row)
