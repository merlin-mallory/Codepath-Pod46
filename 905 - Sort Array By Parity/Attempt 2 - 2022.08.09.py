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
        2. Slow pointer starts at index 0, and iterates right until it finds an odd number.
        3. Fast pointer starts from the slow pointer starts at slow pointer+1, and iterates right until it finds an
        even number. If it reaches the end of the list without finding an even number, return the current array.
        However if it finds an even number, swap the slow pointer's val with the fast pointer's val. And then keep on
        doing slow pointer + 1 until we reach the end of the array.
        """
        # Failed attempt. The fast solution is two pointers at opposite ends of the array. If the left is odd and the
        # right is even, then do the swap. After that, if the left is even, then iterate left++. And if the right is
        # odd, then decrement right--.

        slow = 0

        while slow <= len(nums)-1:
            if nums[slow] % 2 == 0:
                slow += 1
            else:
                fast = slow
                while nums[fast] % 2 == 1 and fast < len(nums)-1:
                    fast += 1

                if nums[fast] % 2 == 0:
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                    slow += 1

        return nums

result = Solution()
print(result.sortArrayByParity([3,1,2,4]))  # [2,4,3,1]
print(result.sortArrayByParity([0]))        # [0]
