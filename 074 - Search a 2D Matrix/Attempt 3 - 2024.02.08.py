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
        Do binary search to find the desired row. The target row will have target >= row[0], but also <= row[-1].
        When we find this row, do binary search a second time to find the desired column. Return true if we find the
        target.
        Otherwise, return False.
        '''
        row_l, row_r = 0, len(matrix)-1
        while row_l <= row_r:
            row_m = (row_l + row_r) // 2
            if target < matrix[row_m][0]:
                row_r = row_m - 1
            elif target > matrix[row_m][-1]:
                row_l = row_l + 1
            else:
                col_l, col_r = 0, len(matrix[row_m])-1
                while col_l <= col_r:
                    col_m = (col_l + col_r) // 2
                    cur_val = matrix[row_m][col_m]
                    if cur_val == target:
                        return True
                    elif cur_val < target:
                        col_l = col_m + 1
                    elif cur_val > target:
                        col_r = col_m - 1
                return False

result = Solution()
print(result.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))  # True
print(result.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)) # False
