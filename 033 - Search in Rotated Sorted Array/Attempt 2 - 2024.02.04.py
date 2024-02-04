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
        1. l = 0, r = len(nums)-1.
        2. Loop while l <= r.
            3. m = (l+r) // 2
            4. m_val = nums[m]
            5. If m_val == target, then return m.
            6. Else if m_val > target, then the target should be to the right, so l = m +1
            7. Otherwise r = m - 1
        8. Return -1
        '''
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            m_val = nums[m]
            if m_val == target:
                return m

            if m_val >= nums[l]:
                # The mid val is in the higher half of the array.
                # Next we need to decide if the target is in the higher half of the array. It could either be to
                # right of mid before the pivot (target > nums[m]) or to left of the left pointer. In either case,
                # we want to search to the right, so set l = m + 1. Otherwise, we will search to the left with r = m -1.
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                # The mid val is in the lower half of the array.
                # Next we need to decide if the target is in the lower half of the array. It could either be to the
                # left of mid before the pivot (target < nums[m]) or right of the right pointer. In either case,
                # we want to search to the left, so set r = m - 1. Otherwise, we will search to the right with r = m
                # + 1.
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1


result = Solution()
print(result.search([4,5,6,7,0,1,2], 0))    # 4
print(result.search([4,5,6,7,0,1,2], 3))    # -1
print(result.search([1], 0))                # -1
