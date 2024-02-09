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
        l,r = 0, len(nums)-1
        Loop while l <= r
            Calculate mid_i, grab mid_v
            If mid_v == target, then return mid_i.
            Next, we will locate the current position of mid_i. If mid_v >= nums[0], then we know that mid_i is in
            the left half of the arary. Next we'll check if the target is to the left of the mid_i. If target <
            mid_v, then we need to search left, so r = mid_i - 1. Otherwise, search right by setting l = mid_i + 1.
            Handle the mirror situation.
        If the loop finishes without returning a mid_i, then we've confirmed that the desired num is not in nums,
        so return -1.
        Time: O(log(n))
        Space: O(1)
        Edge: None
        '''
        l, r = 0, len(nums)-1
        while l <= r:
            mid_i = (l + r) // 2
            mid_v = nums[mid_i]
            if mid_v == target:
                return mid_i
            if mid_v >= nums[0]:
                # mid_i is in the left half of the array.
                if target > mid_v or target < nums[0]:
                    l = mid_i + 1
                else:
                    r = mid_i - 1
            else:
                # mid_i is in the right half of the array.
                if target < mid_v or target > nums[-1]:
                    r = mid_i - 1
                else:
                    l = mid_i + 1
        return -1

result = Solution()
print(result.search([4,5,6,7,0,1,2], 0))    # 4
print(result.search([4,5,6,7,0,1,2], 3))    # -1
print(result.search([1], 0))                # -1
print(result.search([3,5,1], 3))            # 0
print(result.search([3,1], 1))              # 1
