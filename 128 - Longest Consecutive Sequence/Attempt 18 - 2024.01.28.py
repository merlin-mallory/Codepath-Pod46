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
        1. Create nums_set.
        2. Loop through nums and check if the value is a possible start of a sequence, by seeing if nums[i]-1 is in
        the set. If it isn't found, then start a new counter, and scan upwards until the end of the sequence is
        found. And then update longest_consecutive_seq.
        3. Return longest_consecutive_seq
        """
        longest_consecutive_seq = 0
        nums_set = set(nums)
        for num in nums:
            if num-1 not in nums_set:
                counter = 1
                while num+counter in nums_set:
                    nums_set.remove(num+counter)
                    counter += 1
                longest_consecutive_seq = max(longest_consecutive_seq, counter)
        return longest_consecutive_seq
