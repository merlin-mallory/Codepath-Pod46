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
        1. Create a nums_set, and set max_length = 0.
        2. Loop through nums, and try to identify a possible starting number of a sequence. This would be a number-1
        which is not in the set. Then use a counter to scan upwards until a number is not found. Then take the max of the
        current_length and max_length.
        3. Time: O(n), Space: O(n).
        """
        nums_set = set(nums)
        max_length = 0
        for i in range(len(nums)):
            if nums[i]-1 not in nums_set:
                j = i
                current_len = 1
                current_num = nums[i]
                while (current_num+1) in nums_set:
                    current_num += 1
                    current_len += 1
                    j += 1
                max_length = max(max_length, current_len)
        return max_length
