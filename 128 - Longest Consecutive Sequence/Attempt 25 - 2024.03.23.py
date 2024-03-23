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
        Create nums_set, max_len.
        Loop through nums.
            Check if (nums-1) is not in nums_set. If true, then we've found a potential start of a sequence,
            so set counter = 0, and loop upward, increment counter, and remove found values from nums_set. At the end
            of it all, update max_len.
        Return max_len
        Time: O(n)
        Space: O(n)
        Edge: Could be 0 len nums
        """
        nums_set = set(nums)
        max_len = 0
        for i in range(len(nums)):
            if nums_set and ((nums[i]-1) not in nums_set):
                counter = 0
                while nums_set and (nums[i] + counter in nums_set):
                    nums_set.remove(nums[i] + counter)
                    counter += 1
                max_len = max(max_len, counter)
        return max_len