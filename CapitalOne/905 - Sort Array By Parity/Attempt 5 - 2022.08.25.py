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
        3. While left < right, move the left pointer until it finds an odd number, and move the right pointer until
        it finds an even number. When that situation happens, swap the two indexes, and move the pointers. Eventually
        the loop will break somewhere in the middle.
        """

        left, right = 0, len(nums)-1

        while left < right:
            while nums[left] % 2 == 0 and left <= len(nums)-2:
                left += 1

            while nums[right] % 2 == 1 and right >= 1:
                right -= 1

            if nums[left] % 2 == 1 and nums[right] % 2 == 0 and left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums

result = Solution()
print(result.sortArrayByParity([3,1,2,4]))  # [2,4,3,1]
print(result.sortArrayByParity([0]))        # [0]
