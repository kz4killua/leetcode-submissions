class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        board_rows = len(board)
        board_cols = len(board[0])

        for row in range(board_rows):
            for col in range(board_cols):
                if word_search(board, word, set(), (row, col), 0):
                    return True

        return False


def word_search(board, word, path: set[tuple], cell: tuple, i: int):
    board_rows = len(board)
    board_cols = len(board[0])

    if cell in path:
        return False

    row, col = cell
    if board[row][col] != word[i]:
        return False

    if i == (len(word) - 1):
        return True

    # Run word_search() from each of the neighbors
    for r, c in [
        (row + 1, col),
        (row - 1, col),
        (row, col - 1),
        (row, col + 1),
    ]:
        if not ((0 <= r < board_rows) and (0 <= c < board_cols)):
            continue

        if word_search(board, word, path | {cell}, (r, c), i + 1):
            return True

    return False
