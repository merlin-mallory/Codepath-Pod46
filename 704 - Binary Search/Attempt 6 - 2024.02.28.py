from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        704 - Binary Search

        https://leetcode.com/problems/binary-search/

        Given an array of integers nums which is sorted in ascending order, and an integer target, write a function
        to search target in nums. If target exists, then return its index. Otherwise, return -1.

        You must write an algorithm with O(log n) runtime complexity.

        Example 1:
        Input: nums = [-1,0,3,5,9,12], target = 9
        Output: 4
        Explanation: 9 exists in nums and its index is 4

        Example 2:
        Input: nums = [-1,0,3,5,9,12], target = 2
        Output: -1
        Explanation: 2 does not exist in nums so return -1

        Constraints:
        1 <= nums.length <= 10^4
        -10^4 < nums[i], target < 10^4
        All the integers in nums are unique.
        nums is sorted in ascending order.
        Plan:
        Standard binary search
        Time: O(log(n))
        Space: O(1)
        Edge: If target does not exist in nums, return -1.
        '''
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l + r) // 2
            cur = nums[m]
            if cur == target: return m
            elif cur < target: l += 1
            else: r -= 1
        return -1


result = Solution()
print(result.search([-1,0,3,5,9,12], 9))    # 4
print(result.search([-1,0,3,5,9,12], 2))    # -1