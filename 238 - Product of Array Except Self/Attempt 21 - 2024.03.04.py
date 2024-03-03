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
        Init answer to [1]
        Set modifier to 1
        Loop through 1, nums.
            modifier *= nums[i-1]
            answer[i] = prefix
        Set modifier to 1
        Loop through len(nums)-2, -1, -1
            modifier *= nums[i+1]
            answer[i] = answer[i] * modifier
        Return answer
        Time: O(n)
        Space: O(1)
        Edge: None
        '''
        answer = [1] * len(nums)
        modifier = 1
        for i in range(1, len(nums)):
            modifier *= nums[i-1]
            answer[i] = modifier
        modifier = 1
        for i in range(len(nums)-2, -1, -1):
            modifier *= nums[i+1]
            answer[i] = answer[i] * modifier
        return answer

result = Solution()
print(result.productExceptSelf([1,2,3,4]))  # [24,12,8,6]
print(result.productExceptSelf([-1,1,0,-3,3]))  # [0,0,9,0,0]