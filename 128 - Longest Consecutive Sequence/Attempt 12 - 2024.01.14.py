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

        1. Make a minheap.
        2. Pop every element out of the minheap. Check if it is consecutive. If so, update the current_count. When a
        non-consecutive number is found, take the max of current_count and longest_consecutive_sequence. Continue
        until all the elements are popped from the heap.
        3. Return the max consecutive count.
        4. Time: O(nlogn), Space: O(n).

        Plan 2:
        1. Scan the array for the min and max values.
        2. Turn the array into a set.
        3. Loop from min to max, checking if i+1 is in the set, and keep track of current_count and
        longest_consecutive_sequence
        """
        if not nums:
            return 0

        nums_set = set(nums)
        longest_consecutive_sequence = 0

        for num in nums:
            if (num - 1) not in nums_set:
                current_count = 1
                while (num + current_count) in nums_set:
                    current_count += 1

                longest_consecutive_sequence = max(longest_consecutive_sequence, current_count)

        return longest_consecutive_sequence



