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
        1. Create a nums_set.
        2. Loop through nums.
            3. Identify if the current value is a potential start of a sequence, by checking if value-1 is not in
            sequence.
            4. Start a counter, and check the set for sequential numbers. Remove sequential numbers from the set.
            5. Update len_of_sequence.
        6. Return len_of_sequence.
        """
        len_of_max_sequence = 0
        nums_set = set(nums)

        for num in nums:
            if (num-1) not in nums_set:
                len_of_current_sequence = 1
                i = 1
                while (num + i) in nums_set:
                    len_of_current_sequence += 1
                    nums_set.remove(num + i)
                    i += 1
                len_of_max_sequence = max(len_of_max_sequence, len_of_current_sequence)

        return len_of_max_sequence

