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
        Linked List Traversal with Floyd's Algo
        Time: O(n)
        Space: O(1)
        Edge: None
        '''
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow2



solution = Solution()
result = solution.findDuplicate([1,3,4,2,2])
print(result)                                               # 2

new_list_head = solution.findDuplicate([3, 1, 3, 4, 2])
print(new_list_head)                                        # 3

new_list_head = solution.findDuplicate([4,3,1,4,2])
print(new_list_head)                                        # 4
