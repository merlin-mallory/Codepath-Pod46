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

        [1,1,2,6]
        [24,12,4,1]

        Input: nums = [-1,1,0,-3,3]
        Output: [0,0,9,0,0]

        Constraints:
        2 <= nums.length <= 10^5
        -30 <= nums[i] <= 30
        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

        Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as
        extra space for space complexity analysis.)

        Plan:
        1. Initialize prefix and postfix to 1.
        2. Iterate through nums(1,end), and make nums[i] = prefix * nums[i], and make prefix = prefix * nums[i-1]
        3. Iterate backwards from nums(end,-2), and make nums[i] = postfix * nums[i], and make postfix = postfix *
        nums[i+1]
        4. Return the muliplied result of the two subarrays.
        '''

        # Failed attempt. I needed result_arr[i] = prefix, and prefix *= nums[i] to build the prefix. And then for
        # the backwards loop, result_arr[i] = postfix, and postfix *= nums[i]. So the first pass records the previous
        # index's prefix. The second pass takes the value from the first pass and multiplies it by the previous
        # index's postfix. However it's not actually doing [i-1], we're just making it so [i] includes the prefix
        # altered in the [i-1] step.

        prefix, postfix = 1, 1
        result_arr = [1] * len(nums)

        # Prefix calc
        for i in range(1,len(nums)):
            result_arr[i] = prefix * result_arr[i-1]
            prefix = prefix * nums[i]
        print(result_arr)

        # Postfix calc
        for j in range(len(nums)-2, -1, -1):
            result_arr[j] = postfix * result_arr[j+1]
            postfix = postfix * nums[j]
        print(result_arr)

result = Solution()
print(result.productExceptSelf([1,2,3,4]))  # [24,12,8,6]
print(result.productExceptSelf([-1,1,0,-3,3]))  # [0,0,9,0,0]