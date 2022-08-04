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
        """

result = Solution()
print(result.sortArrayByParity([3,1,2,4]))  # [2,4,3,1]
print(result.sortArrayByParity([0]))        # [0]
