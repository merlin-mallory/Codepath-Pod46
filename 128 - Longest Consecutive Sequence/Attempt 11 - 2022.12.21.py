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
        2. Loop through nums, and check if nums[i]-1 is not in nums_set. If it isn't, then it's a candidate for the
        first element of the longest consecutive sequence. So loop while nums[i]+1 is in the set, and update the
        counter. Eventually it will break, and we'll update the lcs counter. Repeat until we reach the end of the
        array, and return the final lcs.
        """
        max_count = 0
        nums_set = set(nums)
        for i in range(len(nums)):
            if (nums[i] - 1) not in nums_set:
                current_num = nums[i]
                current_count = 0
                while current_num in nums_set:
                    current_count += 1
                    current_num += 1
                max_count = max(max_count, current_count)
        return max_count
