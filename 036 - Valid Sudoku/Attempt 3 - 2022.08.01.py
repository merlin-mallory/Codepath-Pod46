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
        1. Create 3 lists of len 9 sets. One for rows, one for columns, one for miniboxes.
        2. Calculation for minibox: m*3 + n//3, where m = rows and n = columns
        3. Loop through board. If the current value is in any of the matching sets, then we've found an invalid
        board, so return False. Otherwise, add the current value to the matching sets.
        4. If we finish looping through the board without return False, then we've validated the board, so return True.
        """

        row_set = [set() for x in range(9)]
        column_set = [set() for x in range(9)]
        box_set = [set() for x in range(9)]

        for m in range(9):
            for n in range(9):
                if board[m][n] in row_set[m]:
                    return False
                elif board[m][n] != ".":
                    row_set[m].add(board[m][n])

                if board[m][n] in column_set[n]:
                    return False
                elif board[m][n] != ".":
                    column_set[n].add(board[m][n])

                box_calc = m//3*3 + n//3
                if board[m][n] in box_set[box_calc]:
                    return False
                elif board[m][n] != ".":
                    box_set[box_calc].add(board[m][n])

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
