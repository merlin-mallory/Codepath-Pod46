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
        1. Loop through nums and find the total_sum.
        2. Create final_arr of size equal to nums.
        3. Loop through nums, take total_sum / nums[i], and assign that to final_arr[i].
        4. I can't do that plan because of restriction.

        Plan 2:
        1. Create final_arr of size equal to nums, with each index initialized to 1.
        2. Loop twice through nums, once from index 1 to end of list, and then once from end of list-1 to
        beginning of list. At each stage multiply the current prefix/postfix.
        '''
        final_arr = [1] * len(nums)
        prefix = 1
        for i in range(0, len(nums)-2):
            prefix *= nums[i]
            final_arr[i+1] = prefix * final_arr[i]

        postfix = 1
        for j in range(len(nums)-1, 0, -1):
            postfix *= nums[j]
            final_arr[j-1] = postfix * final_arr[j]


        return final_arr

result = Solution()
print(result.productExceptSelf([1,2,3,4]))  # [24,12,8,6]
print(result.productExceptSelf([-1,1,0,-3,3]))  # [0,0,9,0,0]

# Neetcode
# res = [1] * (len(nums))
#
# prefix = 1
# for i in range(len(nums)):
#     res[i] = prefix
#     prefix *= nums[i]
# postfix = 1
# for i in range(len(nums) - 1, -1, -1):
#     res[i] *= postfix
#     postfix *= nums[i]
# return res