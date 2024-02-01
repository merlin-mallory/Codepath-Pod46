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
        1. Init max_len = 0, nums_set=set(nums).
        2. Loop through nums.
            3. Check if the num is the start of a sequence by checking if num-1 isn't in the set. If it isn't,
            then start a counter, and increment until the end of the sequence is found. Update the max_len.
            4. Otherwise, just continue.
        5. Return max_len
        Edge Cases: If len(nums) == 0, return 0
        Time: O(n)
        Space: O(n)
        """
        nums_set = set(nums)
        max_len = 0
        for num in nums:
            if num-1 not in nums_set:
                counter = 1
                while num+counter in nums_set:
                    nums_set.remove(num+counter)
                    counter += 1
                max_len = max(max_len, counter)
        return max_len
