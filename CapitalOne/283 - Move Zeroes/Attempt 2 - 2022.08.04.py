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

        1. Loop through nums from left to right. If the current index contains a zero, then search right until a
        non-zero digit is found, and swap the two indexes, and iterate i++. Keep going until we reach the end of the
        list.
        """
        # My attempt worked for small n, but was time limit exceeded. I need to use the two pointers technique,
        # putting the fast pointer in the loop, swapping fast and slow (if fast is pointing to a zero,
        # and slow is pointing to a nonzero), and iterating the slow pointer until it's not pointing at a zero.
        i = 0
        while i < len(nums)-1:
            if nums[i] == 0:
                j = i+1
                while nums[j] == 0 and j < len(nums)-1:
                    j += 1
                nums[i], nums[j] = nums[j], nums[i]
            i += 1

result = Solution()
print(result.moveZeroes([0,1,0,3,12]))  # [1,3,12,0,0]
print(result.moveZeroes([0]))  # [0]
