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
        1. Looks like two pointers. Left = 0, right = len(nums)-1.
        2. Move left to the right, until it finds an even integer. Then move right to the left, until it finds an odd
        integer. Then swap the two, and loop until left >= right.
        """
        left_pointer = 0
        right_pointer = len(nums)-1

        while left_pointer < right_pointer:
            if nums[left_pointer] % 2 == 0:
                left_pointer += 1
            if nums[right_pointer] % 2 == 1:
                right_pointer -= 1
            if nums[left_pointer] % 2 == 1 and nums[right_pointer] % 2 == 0:
                nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
                left_pointer += 1
                right_pointer -= 1
        return nums

result = Solution()
print(result.sortArrayByParity([3,1,2,4]))  # [2,4,3,1]
print(result.sortArrayByParity([0]))        # [0]
