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
        1. Create a prefix_arr of length equal to nums, initalized with 1s. Initialize prefix = nums[0].
        2. Loop through nums, and set prefix_arr[i+1] = prefix * prefix_arr[i+1]. Then update prefix *= prefix_arr[i].
        3. Do the same thing backwards for the suffix.
        4. Return the final result.
        '''
        prefix_arr = [1] * len(nums)
        prefix = nums[0]
        for i in range(1, len(nums)-1):
            prefix_arr[i] = prefix * nums[i]
            prefix *= prefix_arr[i]

        suffix = nums[-1]
        for j in range(len(nums)-2, 0, -1):
            prefix_arr[j-1] = suffix * nums[j]
            suffix = suffix * prefix_arr[j]

        return prefix_arr


result = Solution()
print(result.productExceptSelf([1,2,3,4]))  # [24,12,8,6]
print(result.productExceptSelf([-1,1,0,-3,3]))  # [0,0,9,0,0]