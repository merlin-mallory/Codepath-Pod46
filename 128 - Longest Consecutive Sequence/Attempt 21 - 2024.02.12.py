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
        Create nums_set.
        Loop through nums
            Identify if nums[i]-1 is in nums_set. If so, continue. Otherwise, start a counter, and increment up until
            the end of the set is found, and then update len_of_longest_consecutive.
        Return len_of_longest_consecutive.
        Time: O(n)
        Space: O(1)
        Edge: Nums could be empty, should return 0
        """
        len_of_longest_consecutive = 0
        nums_set = set(nums)
        i = 0
        while i < len(nums):
            if (nums[i]-1) not in nums_set:
                counter = 1
                while (nums[i] + counter) in nums_set:
                    nums_set.remove(nums[i] + counter)
                    counter += 1
                len_of_longest_consecutive = max(len_of_longest_consecutive, counter)
            i += 1
        return len_of_longest_consecutive
