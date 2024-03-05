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
        Binary search through rows to find the target row.
            Binary search through columns to find a match with a target.
                If we find the target, return True.
                If we don't find the target, return False.
            If we don't find the target row, return False
        Guarenteed an answer, so don't need to return anything at end.
        Time: O(log(m*n))
        Space: O(1)
        Edge: None
        '''
        row_l, row_r = 0, len(matrix)-1
        while row_l <= row_r:
            row_m = (row_l + row_r) // 2
            target_row = matrix[row_m]
            if (target >= target_row[0]) and (target <= target_row[-1]):
                # Binary search columns for exact match.
                col_l, col_r = 0, len(target_row)-1
                while col_l <= col_r:
                    col_m = (col_l + col_r) // 2
                    cur = target_row[col_m]
                    if cur < target:
                        col_l = col_m + 1
                    elif cur > target:
                        col_r = col_m - 1
                    else:
                        return True
                return False
            elif (target < target_row[0]):
                row_r = row_m - 1
            else:
                row_l = row_l + 1

result = Solution()
print(result.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))  # True
print(result.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)) # False
