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
        1. Create nums_set, current_consecutive_sequence and longest_consecutive_sequence = 0.
        2. Loop through nums and check for nums[i]-1 and nums[i] in set. Each time a value is found,
        iterate current_consecutive_sequence, and delete the value from the nums_set. We also need to handle
        duplicates.
        3. After we arrive at the end of the current_consecutive_sequence, update the longest_consecutive_sequence.
        """

        nums_set = set(nums)
        longest_consecutive_sequence = 0

        for num in nums:
            current_consecutive_sequence = 1
            temp_num = num
            while (temp_num-1) in nums_set:
                current_consecutive_sequence += 1
                nums_set.discard(temp_num-1)
                temp_num -= 1

            temp_num = num

            while (temp_num+1) in nums_set:
                current_consecutive_sequence += 1
                nums_set.discard(temp_num+1)
                temp_num += 1

            longest_consecutive_sequence = max(longest_consecutive_sequence, current_consecutive_sequence)

        return longest_consecutive_sequence

result = Solution()
print(result.longestConsecutive([100,4,200,1,3,2]))     # 4
print(result.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))  # 9
