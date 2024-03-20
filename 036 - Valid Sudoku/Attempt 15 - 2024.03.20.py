class Solution:
    def isValidSudoku(self, board) -> bool:
        """
        Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the
        following rules:

        Each row must contain the digits 1-9 without repetition.
        Each column must contain the digits 1-9 without repetition.
        Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
        Note:

        A Sudoku board (partially filled) could be valid but is not necessarily solvable.
        Only the filled cells need to be validated according to the mentioned rules.

        Constraints:
        board.length == 9
        board[i].length == 9
        board[i][j] is a digit 1-9 or '.'.

        Plan:
        Hashset
        Create rows, cols, and box arrays. Each contains 9 hashsets.
        Outer loop through rows.
            Inner loop through cols.
                cur = board[r][c]
                Handle "."
                Check if cur is in appropriate index of rows/cols/box. If found, return false. Otherwise, add cur to
                the appropriate set.
                Formula for box_i: ((r // 3) * 3) + (c // 3)
        If we complete the loop without returning False, we've verified the board, so return True.
        Time: O(n)
        Space: O(n)
        Edge: None
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                cur = board[r][c]
                if cur == ".": continue
                if cur in rows[r]:
                    return False
                else:
                    rows[r].add(cur)
                if cur in cols[c]:
                    return False
                else:
                    cols[c].add(cur)
                box_i = ((r // 3) * 3) + (c // 3)
                if cur in boxes[box_i]:
                    return False
                else:
                    boxes[box_i].add(cur)
        return True


result = Solution()

board1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(result.isValidSudoku(board1))  # True

board2 = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(result.isValidSudoku(board2))  # False
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8.
# Since there are two 8's in the top left 3x3 sub-box, it is invalid.

board3 = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
          [".", "4", ".", "3", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", "3", ".", ".", "1"],
          ["8", ".", ".", ".", ".", ".", ".", "2", "."],
          [".", ".", "2", ".", "7", ".", ".", ".", "."],
          [".", "1", "5", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", "2", ".", ".", "."],
          [".", "2", ".", "9", ".", ".", ".", ".", "."],
          [".", ".", "4", ".", ".", ".", ".", ".", "."]]

print(result.isValidSudoku(board3))  # False
