class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        https://leetcode.com/problems/set-matrix-zeroes/
        Do not return anything, modify matrix in-place instead.

        Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

        You must do it in place.

        Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
        Output: [[1,0,1],[0,0,0],[1,0,1]]

        Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

        Constraints:

        m == matrix.length
        n == matrix[0].length
        1 <= m, n <= 200
        -231 <= matrix[i][j] <= 231 - 1

        Follow up:

        A straightforward solution using O(mn) space is probably a bad idea.
        A simple improvement uses O(m + n) space, but still not the best solution.
        Could you devise a constant space solution?

        Plan:
        1. Loop through the matrix, and if a zero is found, then add that index's row to rows_to_be_zeroed_set,
        and add that index's column to the columns_to_be_zeroed set.
        2. Loop through the matrix a second time, and check if the current cell's row is in the rows_to_be_zeroed_set or
        columns_to_be_zeroed_set. If the current cell is in either set, then zero the value.
        3. Time: O(m*n), Space: O(m+n), where m = # of rows, and n = # of columns
        """
        m = len(matrix)
        n = len(matrix[0])

        rows_to_be_zeroed_set = set()
        columns_to_be_zeroed_set = set()

        for row in range(m):
            for column in range(n):
                if matrix[row][column] == 0:
                    rows_to_be_zeroed_set.add(row)
                    columns_to_be_zeroed_set.add(column)

        for row in range(m):
            for column in range(n):
                if row in rows_to_be_zeroed_set:
                    matrix[row][column] = 0
                if column in columns_to_be_zeroed_set:
                    matrix[row][column] = 0

