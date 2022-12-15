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
        1. Create three sets that will confirm board eligibility. row_set, column_set, box_set.
        2. Iterate through the board, check each set to confirm that there is not a duplicate, and then add it to the
        set.
        3. Remember to sanitize for "."
        4. The formula for the box_set is the trickiest part. 3*(row // 3) + (column // 3)?
           (2,2) in box 0? Yes. (2, 3) in box 1? Yes. (2, 8) in box 2? Yes. (3,2) in box 3? Yes.
        """

        row_set, column_set, box_set = [set() for x in range(9)], [set() for x in range(9)], [set() for x in range(9)]
        print("Here:", row_set, column_set, box_set)
        for m in range(9):
            for n in range(9):
                current_val = board[m][n]

                if current_val == ".":
                    continue

                if current_val in row_set[m]:
                    return False
                else:
                    row_set[m].add(current_val)

                if current_val in column_set[n]:
                    return False
                else:
                    column_set[n].add(current_val)

                box_calc = 3 * (m // 3) + (n // 3)

                if current_val in box_set[box_calc]:
                    return False
                else:
                    box_set[box_calc].add(current_val)

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
