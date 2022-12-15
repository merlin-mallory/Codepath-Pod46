class Solution:
    from typing import List
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        """
        Given an array nums of integers and integer k, return the maximum sum such that there exists i < j with nums[
        i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.

        Input: nums = [34,23,1,24,75,33,54,8], k = 60
        Output: 58
        Explanation: We can use 34 and 24 to sum 58 which is less than 60.

        Input: nums = [10,20,30], k = 15
        Output: -1
        Explanation: In this case it is not possible to get a pair sum less that 15.

        Constraints:
        1 <= nums.length <= 100
        1 <= nums[i] <= 1000
        1 <= k <= 2000

        Plan:
        1. Backtracking.
        2. Set the running_list = [], and maximum_sum = 0
        3. If the sum(running_list) == k, then return k. Else if the sum(running_list) > k, then return running_sum
        4. maximum_sum = Add nums[i] to running_sum
        5. running_list.append(nums[i])
        5. maximum_sum = helper(running_list,
        """
        # I gave up. I was overthinking the possibility that there could more than two numbers summed together. But
        # the name of the problem includes two sum, so we only need to consider adding 2 numbers.

        # Real plan is 1. Sort the array, 2. left_pointer = 0, right_pointer = len(nums)-1, max_sum = -1. 3. While
        # left < right, calculate the sum of nums[left] + nums[right]. If the sum is <k, then set max_sum = max(
        # max_sum, sum) and increment left+1. Otherwise, decrement right-1. The max_sum will always contain the maximum
        # value less than k found so far in the array, so we can return that at the end.


result = Solution()
print(result.twoSumLessThanK([34,23,1,24,75,33,54,8], 60))
print(result.twoSumLessThanK([10,20,30], 15))