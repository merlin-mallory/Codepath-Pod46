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
        1. Initialize ret to an array full of 1s, of size len(nums). Initialize prefix to 1, and postfix to 1.
        2. Loop through nums, left to right. ret[i] = prefix. Then prefix = prefix * nums[i].
        3. Loop through nums, right to left. ret[i] = ret[i] * postfix. Then postfix = postfix * nums[i]
        4. Return ret.
        '''

        ret = [1] * len(nums)
        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            ret[i] = prefix
            prefix *= nums[i]

        for j in range(len(nums)-1, -1, -1):
            ret[j] = ret[j] * postfix
            postfix *= nums[j]

        return ret

result = Solution()
print(result.productExceptSelf([1,2,3,4]))  # [24,12,8,6]
print(result.productExceptSelf([-1,1,0,-3,3]))  # [0,0,9,0,0]
