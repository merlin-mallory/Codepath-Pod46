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
        1. Create a final_arr of size len(nums), initialized to 1s. Initialize prefix and postfix to 1.
        2. Loop through final_arr from 0 to end of list. Set final_arr[i] = prefix. Then set prefix = prefix * nums[i].
        3. Loop through final_arr from the end of list to 0. Set final_arr[i] = final_arr[i] * postfix. Then set
        postfix = postfix * nums[i]
        4. Return the final array.
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
