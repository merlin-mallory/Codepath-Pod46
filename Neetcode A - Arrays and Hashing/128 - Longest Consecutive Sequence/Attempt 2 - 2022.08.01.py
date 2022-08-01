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

        1. No idea
        """
        num_set = set(nums)
        max_streak = 0

        for num in num_set:
            if num-1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num+1 in num_set:
                    current_num += 1
                    current_streak += 1

                max_streak = max(max_streak, current_streak)

        return max_streak
