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
        1. l = 0, r = len(matrix)-1.
        1. Calculate mid_row_i = len(matrix) // 2
        2. If matrix[mid_row_i][0] > target, then r = mid_row_i - 1
        3. Else if matrix[mid_row_i[-1] > target, then l = mid_row_i + 1
        5. Else (we found the correct row, so do binary search within the subarray). If we find it, return True.
        Otherwise, return false.
        '''

        l, r = 0, len(matrix)-1
        while l <= r:
            mid_row_i = (l + r) // 2
            if matrix[mid_row_i][0] > target:
                r = mid_row_i - 1
            elif matrix[mid_row_i][-1] < target:
                l = mid_row_i + 1
            else:
                sub_l = 0
                sub_r = len(matrix[mid_row_i])-1
                while sub_l <= sub_r:
                    sub_mid = (sub_r + sub_l) // 2
                    sub_val = matrix[mid_row_i][sub_mid]

                    if sub_val == target:
                        return True
                    elif sub_val < target:
                        sub_l = sub_mid + 1
                    else:
                        sub_r = sub_mid - 1
                return False


result = Solution()
print(result.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))  # True
print(result.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))  # False
