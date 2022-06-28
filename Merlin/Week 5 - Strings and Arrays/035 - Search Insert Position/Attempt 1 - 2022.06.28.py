class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        https://leetcode.com/problems/search-insert-position/description/

        Given a sorted array of distinct integers and a target value, return the index if the target is found.
        If not, return the index where it would be if it were inserted in order.

        You must write an algorithm with O(log n) runtime complexity.

        Input: nums = [1,3,5,6], target = 5
        Output: 2

        Input: nums = [1,3,5,6], target = 2
        Output: 1

        Input: nums = [1,3,5,6], target = 7
        Output: 4

        Constraints:

        1 <= nums.length <= 104
        -104 <= nums[i] <= 104
        nums contains distinct values sorted in ascending order.
        -104 <= target <= 104

        Plan 1:
        1. Create left and right pointers. Call helper function with (nums, target, left, right).
            2. If left > right, then we've verified that the target is not found in the list, so return the right
            index (maybe?)
            3. Calculate the middle index.
            3. Grab middle_val and compare to the target. If we've found the target, then return the target's
            index. Else if the current_val > target, then recursively call to the left (nums, target, left,
            middle-1). Else if the current_val < target, then recursively call to the right (nums, target, middle+1,
            right)
        '''

        def helper(nums, target, left, right):
            if left > right:
                return right+1

            middle = (left + right) // 2
            current_val = nums[middle]
            if current_val == target:
                return middle
            elif current_val < target:
                return helper(nums, target, middle+1, right)
            elif current_val > target:
                return helper(nums, target, left, middle-1)

        len_nums = len(nums) - 1
        return helper(nums, target, 0, len_nums)


