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
        1. Looks like two pointers. Sort the array.
        2. left = 0, right = len(nums)-1, max_sum = -1.
        3. while left < right,
            4. current_sum = nums[left] + nums[right]
            6. if current < k, then take the max of max_sum and current_sum. And then we need to try to make the sum
            bigger, so left++
            7. if current > k, then we need to try to make the sum smaller, so right--
        8. Eventually the loop will break when left exceeds right, and then we return whatever is in max_sum.
        """
        nums.sort()
        left, right, max_sum = 0, len(nums)-1, -1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum < k:
                max_sum = max(max_sum, current_sum)
                left += 1
            else:  # current_sum >= k:
                right -= 1
        return max_sum


result = Solution()
print(result.twoSumLessThanK([34,23,1,24,75,33,54,8], 60))  # 58
print(result.twoSumLessThanK([10,20,30], 15))               # -1