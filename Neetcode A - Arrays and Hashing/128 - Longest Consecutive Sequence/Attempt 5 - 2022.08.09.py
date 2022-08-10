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
        1. Create a hashmap of nums. Set longest_consecutive_len = 1.
        2. Loop through nums, and check if nums[i]-1 is in the hashmap. If it is, then set the substring_len to 2,
        and loop+iterate until a value is not found. Then find the max of longest_consecutive_len and substring_len.
        3. Return the longest_consecutive_len after the loop completes.
        """
        if not nums:
            return 0

        nums_set = set(nums)
        longest_consecutive_len = 1

        for num in nums:
            if num-1 not in nums_set:
                substring_len = 1
                substring_num = num
                while substring_num+1 in nums_set:
                    substring_len += 1
                    substring_num += 1
                longest_consecutive_len = max(longest_consecutive_len, substring_len)

        return longest_consecutive_len
