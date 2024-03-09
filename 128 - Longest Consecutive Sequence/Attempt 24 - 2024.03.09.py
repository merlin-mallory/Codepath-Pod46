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
        Hashset
        Create nums_set, init with nums.
        Set len_of_longest_seq = 0
        Loop through nums.
            Check if (num - 1) is not in nums_set. If so, then we found the potential beginning of a sequence. So set
            counter = 0, and loop upwards until the end of the sequence is found. Remove items from the set at each
            iteration. After the loop breaks, update the len_of_longest_seq with the counter.
        Return len_of_longest_seq.
        Time: O(n)
        Space: O(n)
        Edge: Could be 0 items in nums.
        """
        nums_set = set(nums)
        len_of_longest_seq = 0
        for num in nums:
            if (num-1) not in nums_set:
                counter = 0
                while (num + counter) in nums_set:
                    nums_set.remove(num + counter)
                    counter += 1
                len_of_longest_seq = max(len_of_longest_seq, counter)
        return len_of_longest_seq
