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
        Prefix: [1, 1, 2, 6]
        Postfix: [24, 12, 4, 1]

        Input: nums = [-1,1,0,-3,3]
        Output: [0,0,9,0,0]

        Constraints:
        2 <= nums.length <= 10^5
        -30 <= nums[i] <= 30
        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

        Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as
        extra space for space complexity analysis.)

        1. Create a final_arr of length n, initialized to 1s. Set prefix = 1 and postfix = 1.
        2. Loop through nums (1 to right). final_arr[i] = nums[i-1], and then prefix *= nums[i-1].
        3. Loop through nums (-2 to left). final_arr[i] = nums[i+1], and then prefix *= nums[i+1]
        4. Return the final arr.
        '''
        final_arr = [1] * len(nums)
        prefix, postfix = 1, 1

        for i in range(len(nums)):
            final_arr[i] = prefix
            prefix *= nums[i]

        for j in range(len(nums)-1, -1, -1):
            final_arr[j] = final_arr[j] * postfix
            postfix *= nums[j]

        return final_arr

result = Solution()
print(result.productExceptSelf([1,2,3,4]))  # [24,12,8,6]
print(result.productExceptSelf([-1,1,0,-3,3]))  # [0,0,9,0,0]
