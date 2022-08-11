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
        1. Looks like two pointers. slow = 0.
        2. While slow < len(nums):
            3. If nums[slow] == 0:
                4. Find the next non-zero index, and if one is found, then swap.
            5. Slow++
        6. Return nothing, since we are modifying in-place.
        """
        # Failed attempt. It actually sloves the problem, but there is a faster time complexity solution. Slow starts
        # at 0, fast iterates from 0 to end of list. If nums[slow] = 0 and nums[fast] != 0, then swap. And then,
        # if nums[slow] != 0, then iterate slow++.

        slow = 0
        while slow < len(nums):
            if nums[slow] == 0:
                fast = slow
                while nums[fast] == 0 and fast < len(nums)-1:
                    fast += 1
                if fast == len(nums):
                    return nums
                else:
                    nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
        return nums


result = Solution()
print(result.moveZeroes([0,1,0,3,12]))  # [1,3,12,0,0]
print(result.moveZeroes([0]))  # [0]
