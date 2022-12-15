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
        -2^31 <= matrix[i][j] <= 2^31 - 1

        Follow up:

        A straightforward solution using O(mn) space is probably a bad idea.
        A simple improvement uses O(m + n) space, but still not the best solution.
        Could you devise a constant space solution?

        Plan:
        1. Looks like a hashmap solution.
        2. Loop through matrix[m][n]. If the value is 0, then add m to zeroed_rows_set, and add n to zeroed_columns_set.
        3. Loop through matrix[m][n] a second time, and if either m in zeroed_rows_set or n in zeroed_columns_set,
        then change the cell's value to 0.
        """
        zeroed_rows_set = set()
        zeroed_columns_set = set()

        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if matrix[m][n] == 0:
                    zeroed_rows_set.add(m)
                    zeroed_columns_set.add(n)

        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if m in zeroed_rows_set:
                    matrix[m][n] = 0
                if n in zeroed_columns_set:
                    matrix[m][n] = 0
