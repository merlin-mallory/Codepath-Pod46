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
        1. Create nums_set. Initialize longest_consecutive = 0. current_consecutive = 0
        2. Loop through nums. Check if (nums-1) is not in nums set. If that is true, that means that it is the
        potential beginning of the longest_consecutive set. Loop while (nums+1) is in nums_set. Increment
        current_consecutive +1 for each value found. Eventually when we hit a num not found in the set, update the
        longest_consecutive.
        3. Return the longest_consecutive.
        Time: O(n^2), Space: O(n)
        """
        if not nums:
            return 0

        nums_set = set(nums)
        longest_consecutive = 1

        for i in range(len(nums)):
            if (nums[i] - 1) not in nums_set:
                current_consecutive = 1

                while (nums[i] + current_consecutive) in nums_set:
                    current_consecutive += 1

                longest_consecutive = max(longest_consecutive, current_consecutive)

        return longest_consecutive
