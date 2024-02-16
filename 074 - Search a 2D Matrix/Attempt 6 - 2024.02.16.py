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
        Binary search through rows. Check if we've found the target row (target >= row[0] and target <= row[-1]).
        When we find the target row, binary search the columns for a match. If exact match found, return True,
        otherwise return false.
        Time: O(log(n*m))
        Space: O(1)
        Edge: None
        '''
        row_l, row_r = 0, len(matrix)-1
        while row_l <= row_r:
            row_m = (row_l + row_r) // 2
            cur_row = matrix[row_m]
            if (target >= cur_row[0]) and (target <= cur_row[-1]):
                # We found the target row
                col_l, col_r = 0, len(cur_row)-1
                while col_l <= col_r:
                    col_m = (col_l + col_r) // 2
                    cur_val = cur_row[col_m]
                    if cur_val < target:
                        col_l += 1
                    elif cur_val > target:
                        col_r -= 1
                    else:
                        return True
                return False
            elif target < cur_row[0]:
                row_r = row_m - 1
            else:
                row_l = row_m + 1
        return False


result = Solution()
print(result.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))  # True
print(result.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)) # False
