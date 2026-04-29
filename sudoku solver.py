class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solve(board)

    def solve(self, board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for num in "123456789":
                        if self.isValid(board, r, c, num):
                            board[r][c] = num
                            if self.solve(board):
                                return True
                            board[r][c] = "."
                    return False
        return True

    def isValid(self, board, r, c, num):
        for i in range(9):
            if board[r][i] == num: return False
            if board[i][c] == num: return False
            if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == num: return False
        return True
