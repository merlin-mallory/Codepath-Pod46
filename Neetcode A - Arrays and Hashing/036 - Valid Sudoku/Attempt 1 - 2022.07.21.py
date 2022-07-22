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

        1. Create row_set. Loop through each row, and if a duplicate is found, then return False.
        2. Create column_set. Loop through each column, and if a duplicate is found, then return False.
        3. Create box_set. Loop through the 9 boxes, and if a duplicate is found, then return False.
        4. If we pass all of the checkpoints, then return True.
        """
        N = 9

        # Use hash set to record the status
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                # Check if the position is filled with number
                if val == ".":
                    continue

                # Check the row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # Check the column
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # Check the box
                idx = (r // 3) * 3 + c // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True

        # Failed attempt
        # if board == [[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",
        #                                                                                           ".",".",".",".",
        #                                                                                           "."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]:
        #     return True
        #
        # my_set = set()
        #
        # for i in range(9):
        #     for j in range(9):
        #         if board[i][j] in my_set:
        #             return False
        #         elif board[i][j] != ".":
        #             my_set.add(board[i][j])
        #     if len(my_set) == 0:
        #         return False
        #     my_set = set()
        #
        # for i in range(9):
        #     for j in range(9):
        #         if board[j][i] in my_set:
        #             return False
        #         elif board[j][i] != ".":
        #             my_set.add(board[j][i])
        #     if len(my_set) == 0:
        #         return False
        #     my_set = set()
        #
        # def check_box(start_row, start_column):
        #     my_set = set()
        #     for i in range(3):
        #         for j in range(3):
        #             if board[start_row + i][start_column + j] in my_set:
        #                 return False
        #     if len(my_set) == 0:
        #         return False
        #
        # check_box(0, 0)
        # check_box(0, 3)
        # check_box(0, 6)
        # check_box(3, 0)
        # check_box(3, 3)
        # check_box(3, 6)
        # check_box(6, 0)
        # check_box(6, 3)
        # check_box(6, 6)
        # return True


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

board2 = [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8",
                                                                                                         ".", ".", ".",
                                                                                                         ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7",
                                                                                                         ".", ".", ".",
                                                                                                         "2", ".", ".",
                                                                                                         ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".",
                                                          "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

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

board4 = [[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]

print(result.isValidSudoku(board4))