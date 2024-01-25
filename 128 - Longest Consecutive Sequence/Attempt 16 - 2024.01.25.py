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
        1. Create nums_set.
        2. Loop through nums. Try to find if the current number is the beginning of a sequence, by identifying if
        num-1 exists in nums_set. If such a number is found, then create counter, and scan nums_set to find the
        length of that sequence. And then update len_of_longest_seq.
        3. Return len_of_longest_seq
        Time: O(n) (if we remove found items from the set)
        Space: O(1)
        """
        len_of_longest_seq = 0
        nums_set = set(nums)
        for num in nums:
            if (num-1) not in nums_set:
                counter = 1
                nums_set.remove(num)
                while (num+counter) in nums_set:
                    nums_set.remove(num+counter)
                    counter += 1
                len_of_longest_seq = max(len_of_longest_seq, counter)

        return len_of_longest_seq