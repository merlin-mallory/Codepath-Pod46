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
        1. Create nums_set. longest_consecutive_sequence = 0.
        2. Loop through nums, and check if nums[i]-1 is not in the set. When that happens, we've found a possible
        candidate to form the longest consecutive string. So create a counter, and while loop up until the sequence
        breaks. And then take set the max of longest_consecutive_sequence and counter.
        3. Return longest_consecutive_sequence
        """
        nums_set = set(nums)
        longest_consecutive_sequence = 0

        for i in range(len(nums)):
            current_num = nums[i]
            if current_num-1 not in nums_set:
                counter = 0
                while current_num in nums_set:
                    counter += 1
                    current_num += 1
                longest_consecutive_sequence = max(longest_consecutive_sequence, counter)

        return longest_consecutive_sequence
