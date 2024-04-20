from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        074 - Search a 2D Matrix

        https://leetcode.com/problems/search-a-2d-matrix/

        You are given an m x n integer matrix matrix with the following two properties:

        Each row is sorted in non-decreasing order.
        The first integer of each row is greater than the last integer of the previous row.
        Given an integer target, return true if target is in matrix or false otherwise.

        You must write a solution in O(log(m * n)) time complexity.

        Example 1:
        Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
        Output: true

        Example 2:
        Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
        Output: false

        Constraints:
        m == matrix.length
        n == matrix[i].length
        1 <= m, n <= 100
        -10^4 <= matrix[i][j], target <= 10^4

        Plan:
        Binary Search
        Time: O(log(m *n))
        Space: O(1)
        Edge: None
        '''
        rows, cols = len(matrix), len(matrix[0])
        row_l, row_r = 0, rows-1
        while row_l <= row_r:
            row_m = (row_l + row_r) // 2
            cur_row = matrix[row_m]
            if target < cur_row[0]: row_r = row_m - 1
            elif target > cur_row[-1]: row_l = row_m + 1
            else:
                col_l, col_r = 0, cols-1
                while col_l <= col_r:
                    col_m = (col_l + col_r) // 2
                    cur_val = matrix[row_m][col_m]
                    if cur_val < target: col_l = col_m + 1
                    elif cur_val > target: col_r = col_m - 1
                    else: return True
                return False
        return False

result = Solution()
print(result.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))  # True
print(result.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)) # False
