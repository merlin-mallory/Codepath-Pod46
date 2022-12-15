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

        1. Create empty my_set. Loop through each row in board[m][n]. If board[m][n] in my_set, then return False.
        Otherwise continue. Add board[m][n] to my_set. After we complete each row, empty the set.
        2. Loop through each column in board[m][n]. If board[m][n] in my_set, then return False. Otherwise continue.
        Add board[m][n] to my_set. After we complete each row, empty the set.
        3. Loop through each box in board[m][n]. Make a calculate_box function to take an upper left square,
        and do the same set loop across the selected 3x3 grid. The 9 selected squares will be from a 3x3 loop:
         (0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6).
        """
        my_set = set()
        rows = len(board)
        columns = len(board[0])

        # Check rows for duplicates
        for m in range(rows):
            for n in range(columns):
                if board[m][n] in my_set:
                    return False
                if board[m][n] != ".":
                    my_set.add(board[m][n])
            my_set = set()

        my_set = set()

        # Check columns for duplicates
        for n in range(columns):
            for m in range(rows):
                if board[m][n] in my_set:
                    print("m, n, result", m, n, "False")
                    return False
                if board[m][n] != '.':
                    my_set.add(board[m][n])
            my_set = set()

        def calculate_box(xcoord, ycoord):
            my_set = set()
            for m in range(3):
                for n in range(3):
                    if board[m+xcoord][n+ycoord] in my_set:
                        return False
                    if board[m+xcoord][n+ycoord] != ".":
                        my_set.add(board[m+xcoord][n+ycoord])
            return True

        my_set = set()
        my_result = None

        # Check boxes for duplicates
        for i in range(1, 10, 3):
            for j in range(1, 10, 3):
                my_result = calculate_box(i-1, j-1)
                if my_result is False:
                    return False
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
