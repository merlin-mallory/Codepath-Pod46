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
        1. Sort the array in ascending order.
        2. Set the max_sum to -1.
        3. Use the two pointer technique to iterate through the array to find the max sum. Calculate nums[
        left_pointer] + nums[right_pointer]. If the result is less than k and greater than max_sum, then set max_sum
        to the result, and increment the left_pointer by 1. If the max_sum is greater than the result, then discard
        the result, and increment the left_pointer by 1. If the result is greater than k, then decrement the
        right_pointer by 1. This loop will end when the pointers equal each other.
        """

        nums.sort()
        max_sum, left_pointer, right_pointer = -1, 0, len(nums)-1

        while left_pointer != right_pointer:
            current_sum = nums[left_pointer] + nums[right_pointer]
            if current_sum < k:
                max_sum = max(max_sum, current_sum)
                left_pointer += 1
            else:  # current_sum <= k
                right_pointer -= 1

        return max_sum



result = Solution()
print(result.twoSumLessThanK([34,23,1,24,75,33,54,8], 60))  #58
print(result.twoSumLessThanK([10,20,30], 15))  #-1
