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
        1. Looks like slow/fast pointers.
        2. slow = 0, fast = loop from 0 to end of array.
        3. Move the slow pointer until it points to a zero or reaches the end of the array.
        4. If the fast pointer > slow pointer and the fast pointer is pointing to a non-zero, then swap the indexes
        between the two pointers.
        5. Return the resultant nums
        """
        slow = 0
        for fast in range(len(nums)):
            while nums[slow] != 0 and slow < len(nums)-1:
                slow += 1

            if fast > slow and nums[fast] != 0 and nums[slow] == 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]

        return nums

result = Solution()
print(result.moveZeroes([0,1,0,3,12]))  # [1,3,12,0,0]
print(result.moveZeroes([0]))  # [0]
