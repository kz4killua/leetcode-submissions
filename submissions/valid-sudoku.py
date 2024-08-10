class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        subs = [set() for i in range(9)]

        for r in range(9):
            for c in range(9):
                s = (c // 3) + 3 * (r // 3)

                if board[r][c] == ".":
                    continue

                if board[r][c] in rows[r]:
                    return False
                if board[r][c] in cols[c]:
                    return False
                if board[r][c] in subs[s]:
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                subs[s].add(board[r][c])

        return True
