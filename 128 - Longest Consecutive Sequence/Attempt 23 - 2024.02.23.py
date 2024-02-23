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
        Hashmap
        Create nums_set. Init with nums.
        Loop through nums.
            Check if num-1 is not in nums_set. If so, then we found the potential beginning of a sequence. So create
            a counter, and loop upwards until the end of the sequence is found, incrementing the counter each step.
            After the loop completes, update max_len.
        Return max_len
        Time: O(n)
        Space: O(1)
        Edge: len(nums) can be 0.
        """
        max_len = 0
        nums_set = set(nums)
        for num in nums:
            if (num - 1) not in nums_set:
                counter = 0
                while (num + counter) in nums_set:
                    counter += 1
                max_len = max(max_len, counter)
        return max_len