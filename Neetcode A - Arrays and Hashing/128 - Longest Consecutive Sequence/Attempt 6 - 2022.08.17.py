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
        1. Convert nums into a set. Initialize longest_consecutive_sequence to 0.
        2. Loop through nums, and check if nums[i]-1 is in the set. If it isn't, then it's a candidate for the
        longest consecutive sequence. Create a counter and loop forward + 1 until the consecutive sequence breaks.
        """
        longest_consecutive_sequence = 0
        nums_set = set(nums)
        for i in range(len(nums)):
            current_val = nums[i]
            if current_val-1 not in nums_set:
                counter = 0
                explore_val = current_val
                while explore_val in nums_set:
                    counter += 1
                    explore_val += 1
                longest_consecutive_sequence = max(longest_consecutive_sequence, counter)
        return longest_consecutive_sequence
