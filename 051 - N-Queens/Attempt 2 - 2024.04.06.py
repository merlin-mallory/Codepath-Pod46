from typing import List
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

        Plan:
        Backtracking
        Time: O(2^n)
        Space: O(n)
        Edge: None
        '''
        c_set = set()
        neg_diag_set = set()
        pos_diag_set = set()
        rows, cols = n, n
        final_arr = []
        board = []
        for _ in range(rows):
            row = []
            for _ in range(cols):
                row.append(".")
            board.append(row)

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                final_arr.append(copy)
                return
            for c in range(cols):
                if (c in c_set) or (r-c in neg_diag_set) or (r+c in pos_diag_set):
                    continue
                c_set.add(c)
                neg_diag_set.add(r-c)
                pos_diag_set.add(r+c)
                board[r][c] = "Q"
                backtrack(r+1)
                board[r][c] = "."
                pos_diag_set.remove(r+c)
                neg_diag_set.remove(r-c)
                c_set.remove(c)
        backtrack(0)
        return final_arr


result = Solution()
print(result.solveNQueens(4))   # [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
print(result.solveNQueens(1))   # [["Q"]]
