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
        1. Looks like two pointers.
        2. Left = 0, right = len(nums)-1
        3. while left < right:
            4. Move left pointer until it points at an odd number.
            5. Move right pointer until it points to an even number.
            6. If left pointer is pointing to odd and right pointer is pointing to even, then swap left and right,
            and iterate left++ and decrement right--.
        7. Return the array.
        """
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] % 2 == 1 and nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

            if nums[left] % 2 == 0:
                left += 1

            if nums[right] % 2 == 1:
                right -= 1

        return nums

result = Solution()
print(result.sortArrayByParity([3,1,2,4]))  # [2,4,3,1]
print(result.sortArrayByParity([0]))        # [0]
