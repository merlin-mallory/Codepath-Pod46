from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the
        non-zero elements.

        Note that you must do this in-place without making a copy of the array.

        Input: nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]

        Input: nums = [0]
        Output: [0]

        Constraints:

        1 <= nums.length <= 10^4
        -2^31 <= nums[i] <= 2^31 - 1

        Plan:
        1. Looks like sliding window.
        2. Slow pointer starts at 0, fast pointer iterates from index 0 to end of array.
        3. If slow is pointing to 0 and fast is pointing to non-zero, then swap slow and fast.
        4. Then iterate slow until it finds the next zero.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            if nums[slow] != 0 and slow < len(nums)-1:
                slow += 1

result = Solution()
print(result.moveZeroes([0,1,0,3,12]))  # [1,3,12,0,0]
print(result.moveZeroes([0]))  # [0]
