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
        1. l = 0, r = len(nums)-1
        2. Loop while l <= r.
            3. Calculate mid. m = (l+r) // 2.
            4. Check if mid == target. If so, return true.
            5. Otherwise, check if mid > nums[l]. If so, then the left part of the array must contain values less
            then mid. If the target is < mid, then we want to search the left half by setting r = mid - 1. Otherwise,
            we should search the right half, by setting l = mid + 1.
        6. If the loop finishes without finding the target, then we've confirmed that the target is not in the array,
        so return False.
        '''
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m

            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1

result = Solution()
print(result.search([4,5,6,7,0,1,2], 0))    # 4
print(result.search([4,5,6,7,0,1,2], 3))    # -1
print(result.search([1], 0))                # -1