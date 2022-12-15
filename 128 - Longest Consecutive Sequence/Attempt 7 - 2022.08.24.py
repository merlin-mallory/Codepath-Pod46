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
        1. Create nums_set. Initialize longest_consecutive_sequence = 0.
        2. Loop through nums, and check if nums[i]-i is not in num_set. If that's the case, then it's a candidate for
        the longest maximum sequence, so start a counter at one, and loop forward until the sequence breaks. Then
        find the max of (longest_consecutive_sequence and current_consecutive_sequence).
        """
        if not nums:
            return 0

        nums_set = set(nums)
        longest_consecutive_sequence = 0

        for i in range(len(nums)):
            if nums[i]-1 not in nums_set:
                current_consecutive_sequence = 0
                j = nums[i]
                while j in nums_set:
                    current_consecutive_sequence += 1
                    j += 1
                longest_consecutive_sequence = max(longest_consecutive_sequence, current_consecutive_sequence)

        return longest_consecutive_sequence

