from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/sort-array-by-parity/

        Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd
        integers.

        Return any array that satisfies this condition.

        Input: nums = [3,1,2,4]
        Output: [2,4,3,1]
        Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

        Input: nums = [0]
        Output: [0]

        Constraints:
        1 <= nums.length <= 5000
        0 <= nums[i] <= 5000

        Plan:
        1. Loop through nums and count the number of odd integers.
        2. Until the current_count = odd_int_count, loop through nums, pop the odd values from the list, and append
        them to the end of the list.
        """
        # My attempt succeeds, but it's kinda slow at O(n^2) time complexity. It is possible to do O(n) time O(1)
        # space by modifying in-place.
        odd_count = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                odd_count += 1

        current_count = 0
        i = 0
        while current_count < odd_count and i < len(nums):
            if nums[i] % 2 == 1:
                temp = nums.pop(i)
                nums.append(temp)
                current_count += 1
            else:
                i += 1

        return nums

        # In-place modification solution:
        # i, j = 0, len(A) - 1
        # while i < j:
        #     if A[i] % 2 > A[j] % 2:
        #         A[i], A[j] = A[j], A[i]
        #
        #     if A[i] % 2 == 0: i += 1
        #     if A[j] % 2 == 1: j -= 1
        #
        # return A


result = Solution()
print(result.sortArrayByParity([3, 1, 2, 4]))  # [2,4,3,1]
print(result.sortArrayByParity([0]))  # [0]
