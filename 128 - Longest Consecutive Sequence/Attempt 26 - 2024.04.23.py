from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/longest-consecutive-sequence/

        Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

        You must write an algorithm that runs in O(n) time.

        Input: nums = [100,4,200,1,3,2]
        Output: 4
        Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

        Input: nums = [0,3,7,2,5,8,4,6,0,1]
        Output: 9

        Constraints:
        0 <= nums.length <= 10^5
        -10^9 <= nums[i] <= 10^9

        Plan:
        Hashset
        Time: O(n)
        Space: O(n)
        Edge: Nums could be empty
        """
        nums_set = set(nums)
        max_len = 0
        for i in range(len(nums)):
            if (nums[i]-1) not in nums_set:
                count = 0
                while (nums[i] + count) in nums_set:
                    nums_set.remove(nums[i]+count)
                    count += 1
                max_len = max(max_len, count)
        return max_len
