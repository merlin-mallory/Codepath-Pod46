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
        1. Looks like two pointers
        2. Set the front_pointer = 0. Set back_pointer = len(nums)-1.
        3. Create a loop where as long as front_pointer < back_pointer:
            4. If nums[front_pointer] is odd and nums[backpointer] is even, then swap the two.
            4. If nums[front_pointer] is even, then iterate front_pointer+1
            5. If nums[back_pointer] is odd, then decrement back_pointer-1
        6. Return the result
        """

        front_pointer = 0
        back_pointer = len(nums)-1
        while front_pointer < back_pointer:
            if (nums[front_pointer] % 2 == 1) and (nums[back_pointer] % 2 == 0):
                nums[front_pointer], nums[back_pointer] = nums[back_pointer], nums[front_pointer]
            if nums[front_pointer] % 2 == 0:
                front_pointer += 1
            if nums[back_pointer] % 2 == 1:
                back_pointer -= 1

        return nums

result = Solution()
print(result.sortArrayByParity([3,1,2,4]))  # [4,2,1,3]
print(result.sortArrayByParity([0]))        # [0]
