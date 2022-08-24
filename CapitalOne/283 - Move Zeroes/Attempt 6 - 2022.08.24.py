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
        1. Looks like fast/slow pointers.
        2. slow_pointer starts at 0, and moves right until nums[slow_pointer] != 0.
        3. fast_pointer loops from 0 to len(nums)-1
        4. if nums[slow_pointer] == 0 and nums[fast_pointer] != 0, then swap, and move slow_pointer +1.
        """

        slow_pointer = 0
        for fast_pointer in range(len(nums)):
            while nums[slow_pointer] != 0 and slow_pointer < len(nums)-1:
                slow_pointer += 1

            if nums[slow_pointer] == 0 and nums[fast_pointer] != 0 and slow_pointer < fast_pointer:
                nums[slow_pointer], nums[fast_pointer] = nums[fast_pointer], nums[slow_pointer]



result = Solution()
print(result.moveZeroes([0,1,0,3,12]))  # [1,3,12,0,0]
print(result.moveZeroes([0]))  # [0]
