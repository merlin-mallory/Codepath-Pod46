from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
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

        Plan:
        Binary Search
        1. row_l = 0, row_r = len(matrix)
        2. Loop while row_l < row_r.
            3. Calculate row_m = (row_l + row_m) // 2.
            4. Check if target < row_m[0], in which case row_r = row_m - 1.
            5. Else if target > row_m[-1], in which case row_l = row_m + 1.
            6. Else we've found the correct row, so now we binary search with col_l = 0, and col_r = len(matrix[
            0])-1. When we find the target, return True.
        7. Return False
        '''
        row_l, row_r = 0, len(matrix)-1
        while row_l <= row_r:
            row_m = (row_l + row_r) // 2
            if target < matrix[row_m][0]:
                row_r = row_m - 1
            elif target > matrix[row_m][-1]:
                row_l = row_l + 1
            else:
                col_l, col_r = 0, len(matrix[0])-1
                while col_l <= col_r:
                    col_m = (col_l + col_r) // 2
                    if target == matrix[row_m][col_m]:
                        return True
                    elif matrix[row_m][col_m] < target:
                        col_l = col_m + 1
                    elif matrix[row_m][col_m] > target:
                        col_r = col_m - 1
                return False

result = Solution()
print(result.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))  # True
print(result.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)) # False
