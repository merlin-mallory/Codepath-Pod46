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
        1. Loop through the array backwards, from (len(nums)-1 to -1). Check if nums[i] is 0. If it is,
        then swap nums[i] and nums[i+1] until nums[i+1] is either zero, or we've reached the end of the list.
        2. This seems like a n^2 solution though, and nums can be quite large, so I'm going to skip to solution.
        """
        # This solution uses the two pointers technique. The slow pointer starts at 0, and the fast pointer loops
        # through the length of nums. At iteration, check if the fast pointer is pointing to a non-zero int and the
        # slow pointer is pointing to a zero int. In this case, there is a zero that is too far to the left of the
        # list, so swap the values at the slow pointer and fast pointers. After a swap occurs, increment the slow
        # pointer until it reaches the next zero value. Then the loop will repeat, and search for a swap with the
        # next non-zero element in the list.

        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                print("Nums after swap:", nums)

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1
                print("slow+1")

        return

result = Solution()
print(result.moveZeroes([0,1,0,3,12]))  # [1,3,12,0,0]
print(result.moveZeroes([0]))  # [0]
