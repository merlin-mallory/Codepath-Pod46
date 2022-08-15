from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        https://leetcode.com/problems/product-of-array-except-self/

        Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the
        elements of nums except nums[i].

        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

        You must write an algorithm that runs in O(n) time and without using the division operation.

        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]

        Input: nums = [-1,1,0,-3,3]
        Output: [0,0,9,0,0]

        Constraints:
        2 <= nums.length <= 10^5
        -30 <= nums[i] <= 30
        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

        Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as
        extra space for space complexity analysis.)

        Plan:
        1. Initialize prefix to 1 and postfix to 1.
        2. Loop through nums[1:], multiplying nums[i-1] * prefix, and then prefix *= nums[i-1]
        3. Loop backwards through nums[:-2], multiplying nums[i+1] * postfix, and then postfix *= nums[i+1]
        4. Return the final array
        '''
        # Failed attempt. I should initialize a new return array initialized to 1s, instead of modifying the existing
        # array. Set the res[i] to prefix first, and then multiply prefix * nums[i].

        prefix = 1
        postfix = 1

        for i in range(1, len(nums)):
            temp = nums[i]
            nums[i] = prefix * nums[i-1]
            prefix *= temp

        for j in range(len(nums)-2, -1, -1):
            temp = nums[j]
            nums[j] = postfix * nums[j+1]
            postfix *= temp

        return nums

result = Solution()
print(result.productExceptSelf([1,2,3,4]))  # [24,12,8,6]
print(result.productExceptSelf([-1,1,0,-3,3]))  # [0,0,9,0,0]