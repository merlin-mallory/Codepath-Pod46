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
        1. row = m = len(matrix)
        2. column = n = len(matrix[0])
        3. set_of_zeroed_rows = set()
        4. set_of_zeroed_columns = set()
        5. for i in range m:
        6.  for j in range n:
        7.      if matrix[i][j] == 0, add i to set of zeroed_rows, and j to set of zeroed_columns
        8. for i in range m:
        9.  for j in range n:
        10.     if i in set_of_zeroed_zeros or j in set_of_zeroed_columns:
        11.         matrix[i][j] = 0
        12. Return matrix
        """

        m = len(matrix)
        n = len(matrix[0])
        set_of_zeroed_rows = set()
        set_of_zeroed_columns = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    set_of_zeroed_rows.add(i)
                    set_of_zeroed_columns.add(j)

        for i in range(m):
            for j in range(n):
                if (i in set_of_zeroed_rows) or (j in set_of_zeroed_columns):
                    matrix[i][j] = 0

        return matrix
