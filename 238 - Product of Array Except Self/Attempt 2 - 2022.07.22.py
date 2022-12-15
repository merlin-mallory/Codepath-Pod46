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
        1. Create a prefix array, which will store [1, 1, 2, 6]
        2. Create a postfix array, which will store [24, 12, 4, 1]
        3. Loop through prefix, and prefix[i] = prefix[i] * postfix[i]
        4. Return prefix array.
        '''

        prefix_array = [0] * len(nums)
        postfix_array = [0] * len(nums)

        prefix_array[0] = 1
        for i in range(1, len(nums)):
            prefix_array[i] = prefix_array[i-1] * nums[i-1]

        # print("prefix:", prefix_array)

        postfix_array[-1] = 1
        print("postfix p1", postfix_array)
        for i in range(len(nums)-2, -1, -1):
            # print("i is", i)
            postfix_array[i] = postfix_array[i+1] * nums[i+1]

        # print("postfix:", postfix_array)

        # Multiply together
        for i in range(len(nums)):
            prefix_array[i] *= postfix_array[i]

        return prefix_array
