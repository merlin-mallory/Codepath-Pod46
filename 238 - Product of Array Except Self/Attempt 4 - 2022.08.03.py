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
        1. Create a prefix_arr and postfix_arr, of size len(nums), initialized to 1s
        2. Loop through nums(0,len(nums), and fill up the prefix_arr. prefix_arr[i+1] = prefix_arr[i] * nums[i+1].
        3. Loop through nums(len(nums), -1, -1), and fill up the postfix_arr. postfix_arr[i-1] = prefix_arr[i] *
        nums[i-1].
        4. Loop through prefix_arr and multiply prefix_arr[i] * postfix_arr[i]
        5. Return the prefix_arr, which should contain the final result.
        '''


        # Failed attempt. I didn't actually need to create two arrays. I just needed one for the response. It was
        # possible to just use a single variable
        # to store the prefix/postfix, and just loop through the array, updating nums[i] with the prefix first,
        # and then updating prefix *= nums[i] second. And then after the prefix loops finishes, create postfix = 1,
        # and loop backwards, again updating res[i] first, and postfix *= nums[i] second. Then the res contains the
        # final result.

        # prefix_arr = [1] * len(nums)
        # postfix_arr = [1] * len(nums)
        #
        # # Filling up the prefix arr
        # for i in range(1, len(nums)):
        #     prefix_arr[i] = prefix_arr[i-1] * nums[i]
        # print("prefix_arr:", prefix_arr)
        #
        # # Filling up the postifx arr
        # for j in range(len(nums)-1, 0, -1):
        #     postfix_arr[j] = postfix_arr[j+1] * nums[j]
        # print("postfix_arr:", postfix_arr)
        #
        # # Combining the two arrs
        # for k in range(len(nums)):
        #     prefix_arr[k] = prefix_arr[k] * postfix_arr[k]
        # return prefix_arr

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

result = Solution()
print(result.productExceptSelf([1,2,3,4]))  # [24,12,8,6]
print(result.productExceptSelf([-1,1,0,-3,3]))  # [0,0,9,0,0]
