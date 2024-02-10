from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        287 - Find the Duplicate Number

        https://leetcode.com/problems/find-the-duplicate-number/

        Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

        There is only one repeated number in nums, return this repeated number.

        You must solve the problem without modifying the array nums and uses only constant extra space.

        Example 1:
        Input: nums = [1,3,4,2,2]
        Output: 2

        Example 2:
        Input: nums = [3,1,3,4,2]
        Output: 3

        Constraints:
        1 <= n <= 105
        nums.length == n + 1
        1 <= nums[i] <= n
        All the integers in nums appear only once except for precisely one integer which appears two or more times.

        Follow up:
        How can we prove that at least one duplicate number must exist in nums?
        Can you solve the problem in linear runtime complexity?

        Plan:
        Floyd's Algorithm. Start both pointer
        '''
        # Phase 1: Find intersection point of the two runners. Floyd's algo starts both slow and fast at zero,
        # and accesses indexes to traverse the list. Eventually we will hit a point where slow = fast, which will be
        # equal to the distance between the beginning of the list and the start of the cycle.
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # At this point the slow and fast pointers will be at a distance equal to the distance between index 0 and
        # the start of the cycle.

        # Phase 2: Find the "entrance" to the cycle.
        slow2 = 0  # Start over from the beginning.
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        # Eventually slow2 will advance to the beginning of the cycle, and it will intersect with slow2.

solution = Solution()
result = solution.findDuplicate([1,3,4,2,2])
print(result)                                               # 2

new_list_head = solution.findDuplicate([3, 1, 3, 4, 2])
print(new_list_head)                                        # 3

new_list_head = solution.findDuplicate([4,3,1,4,2])
print(new_list_head)                                        # 4
