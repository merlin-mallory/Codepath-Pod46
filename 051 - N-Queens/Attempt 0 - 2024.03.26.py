class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        051 - N-Queens

        https://leetcode.com/problems/n-queens/

        The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack
        each other.

        Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any
        order.

        Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both
        indicate a queen and an empty space, respectively.

        Example 1:
        Input: n = 4
        Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
        Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

        Example 2:
        Input: n = 1
        Output: [["Q"]]

        Constraints:
        1 <= n <= 9
        '''
        col_set = set()
        pos_diag_set = set()
        neg_diag_set = set()
        final_arr = []
        board = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(".")
            board.append(row)
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                final_arr.append(copy)
                return
            for c in range(n):
                if (c in col_set) or (r+c in pos_diag_set) or (r-c in neg_diag_set):
                    continue
                col_set.add(c)
                pos_diag_set.add(r+c)
                neg_diag_set.add(r-c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col_set.remove(c)
                pos_diag_set.remove(r + c)
                neg_diag_set.remove(r - c)
                board[r][c] = "."
        backtrack(0)
        return final_arr