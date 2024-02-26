from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        033 - Search in Rotated Sorted Array

        https://leetcode.com/problems/search-in-rotated-sorted-array/

        There is an integer array nums sorted in ascending order (with distinct values).

        Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k
        (1 <= k < nums.length) such that the resulting array is
        [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).

        For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

        Given the array nums after the possible rotation and an integer target, return the index of target if it is
        in nums, or -1 if it is not in nums.

        You must write an algorithm with O(log n) runtime complexity.

        Example 1:
        Input: nums = [4,5,6,7,0,1,2], target = 0
        Output: 4

        Example 2:
        Input: nums = [4,5,6,7,0,1,2], target = 3
        Output: -1

        Example 3:
        Input: nums = [1], target = 0
        Output: -1

        Constraints:
        1 <= nums.length <= 5000
        -10^4 <= nums[i] <= 10^4
        All values of nums are unique.
        nums is an ascending array that is possibly rotated.
        -10^4 <= target <= 10^4

        Plan:
        Binary Search
        l, r = 0, len(nums)-1.
        Loop while l <= r.
            Calc m, cur
            Case 1: If cur == target, return m
            Case 2: If cur >= nums[0], then m is in the left segment.
                If target >= nums[0] and target < cur, then search left with r = m-1. Otherwise, the target could be
                in either the left segment to the right of cur, or in the right segment, so search right with l = m+1.
            Case 3: If cur < nums[0], then m is in the right segment.
                Do the mirror of case 2
        Return -1
        Time: O(log (n))
        Space: O(1)
        Edge: None
        '''
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l + r) // 2
            cur = nums[m]
            if cur == target:
                return m
            elif cur >= nums[0]:
                # m is in left seg.
                if (target >= nums[0]) and (target < cur):
                    r = m - 1
                else:
                    l = m + 1
            else:
                # m is in right seg.
                if (target <= nums[-1]) and (target > cur):
                    l = m + 1
                else:
                    r = m - 1
        return -1


result = Solution()
print(result.search([4,5,6,7,0,1,2], 0))    # 4
print(result.search([4,5,6,7,0,1,2], 3))    # -1
print(result.search([1], 0))                # -1
print(result.search([3,5,1], 3))            # 0
print(result.search([3,1], 1))              # 1
