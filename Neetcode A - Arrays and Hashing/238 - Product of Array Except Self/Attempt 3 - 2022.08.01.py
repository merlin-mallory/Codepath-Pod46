class Solution:
    def productExceptSelf(self, nums):
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
        1. Make 2 arrays of len(nums). prefix_arr stores the values from left to right. suffix_arr stores the values
        from right to left. Loop through nums and create prefix_arr and suffix_arr. Then loop through prefix_arr and
        multiply it by the same index in suffix_arr.
        '''
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

        # Failed Attempt
        # prefix_arr = [0] * len(nums)
        # suffix_arr = [0] * len(nums)
        #
        # # Construct prefix
        # prefix_arr[0] = 1
        # for i in range(1,len(nums)):
        #     prefix_arr[i] = prefix_arr[i-1] * nums[i-1]
        #
        # # Construct suffix
        # suffix_arr[0] = 1
        # for j in reversed(range(len(nums))):
        #     suffix_arr[j] = suffix_arr[j] * nums[j-1]
        #
        # print(prefix_arr, suffix_arr)


result = Solution()
result.productExceptSelf([1,2,3,4])