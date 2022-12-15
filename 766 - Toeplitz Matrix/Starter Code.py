class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        '''
        https://leetcode.com/problems/toeplitz-matrix/description/

        Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
        A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

        Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
        Output: true
        Explanation:
        In the above grid, the diagonals are:
        "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
        In each diagonal all elements are the same, so the answer is True.

        Input: matrix = [[1,2],[2,2]]
        Output: false
        Explanation:
        The diagonal "[1, 2]" has different elements.

        Constraints:

        m == matrix.length
        n == matrix[i].length
        1 <= m, n <= 20
        0 <= matrix[i][j] <= 99

        Follow up:

        What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row
        of the matrix into the memory at once? What if the matrix is so large that you can only load up a partial row
        into the memory at once?

        Plan:
        1. row = m = len(matrix)-1
        2. column = n = len(matrix[0])-1
        3. current = bottom left cell of matrix [len(matrix)-1][0]
        4. if [len(matrix)-2][0] != [len(matrix)-1][1] return False
        5. if [len(matrix)-3][0] != [len(matrix)-2][1] != [len(matrix-1)][2] return False
        6. if [len(matrix)-3][1] != [len(matrix-2][2] != [len(matrix-1)][3] return False
        7. Start in the bottom right cell. Call is_toeplitz(row, column) to check if that square is toeplitz. Then
        iterate backwards through [row][0] until the top row is hit. Then call is_toeplitz on all the remain cells in
        the top row. If there's a mismatch at any time, return False. Otherwise, after we explore the entire matrix,
        we can return true.
        '''

        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if (r-c) not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True

        # max_row = len(matrix)-1
        # max_column = len(matrix[0])
        #
        # current_row = max_row
        # current_column = 0
        #
        # def is_toeplitz(matrix, current_row, current_column, max_row, max_column):
        #     while current_row > 0 and current_column < max_column:
        #
        #
        #
        #
        # for i in range(max_row):
        #     if is_toeplitz(matrix, current_row, current_column, max_row, max_column):
        #         current_row -= 1
        #     else:
        #         return False
        #
        # current_row += 1
        #
        # for j in range(max_column):
        #     if is_toeplitz(matrix, current_row, current_column, max_row, max_column):
        #         current_column += 1
        #     else:
        #         return False
        #
        # return True



