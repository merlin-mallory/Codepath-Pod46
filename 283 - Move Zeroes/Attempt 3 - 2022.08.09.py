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
        1. Two pointers. One pointing to each end of the list. Iterate the left pointer until it finds a zero. Then
        iterate the right pointer until it finds a non-zero. Swap those two indices, and continue iterating until
        left=right pointer, at which point we should have a perfectly swapped array.
        2. Time: O(n), Space: O(1)
        """
        # Failed attempt. My solution did move all of the zeros to the end of the array, however it did not preserve
        # the order of nonzeros. It looks like two pointers is the right idea, but instead of starting at opposite
        # sides of the array, they should start on the same side. The slow will collect all the zeros on the left
        # side, and the fast will progressively check the next index for nonzeros pairs to confirm a swap.
        left_pointer, right_pointer = 0, len(nums)-1

        while left_pointer < right_pointer:
            if nums[left_pointer] != 0:
                left_pointer += 1

            if nums[right_pointer] == 0:
                right_pointer -= 1

            if nums[left_pointer] == 0 and nums[right_pointer] != 0:
                nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
                left_pointer += 1
                right_pointer -= 1

        return

result = Solution()
print(result.moveZeroes([0,1,0,3,12]))  # [1,3,12,0,0]
print(result.moveZeroes([0]))  # [0]
