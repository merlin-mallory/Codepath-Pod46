import copy


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

        1. Create ret[0]*len(nums).
        2. Loop through nums, calculate the total_product, and count the number of zeros, and record the index of the
        zero.
        3. If there are no zeroes, then loop through nums, ret[i] = total_product/nums[i].
        4. If there is one zero, then make a copy, pop that index, and calculate the zero_total_product of the
        remaining numbers. Then make ret[index of zero] = zero_total_product.
        5. If there are multiple zeros, then we will be returning an array of zeros, so no further modifications need.
        6. Return ret.
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

        # I misread the problem, I can't use the division operation
        # ret = [0] * len(nums)
        #
        # current_product = 1
        # num_of_zeroes = 0
        # index_of_zero = -1
        #
        # for i in range(len(nums)):
        #     current_product = current_product * nums[i]
        #     if nums[i] == 0:
        #         num_of_zeroes += 1
        #         index_of_zero = i
        #
        # if num_of_zeroes == 0:
        #     for j in range(len(nums)):
        #         current_val = current_product / nums[j]
        #         ret[j] = int(current_val)
        # elif num_of_zeroes == 1:
        #     zero_list = copy.deepcopy(nums)
        #     zero_list.pop(index_of_zero)
        #     zeroed_product = 1
        #     for k in range(len(zero_list)):
        #         zeroed_product = zeroed_product * zero_list[k]
        #     ret[index_of_zero] = int(zeroed_product)
        #
        # return ret

    # Neetcode
    #         res = [1] * (len(nums))
    #         prefix = 1
    #         for i in range(len(nums)):
    #             res[i] = prefix
    #             prefix *= nums[i]
    #         postfix = 1
    #         for i in range(len(nums) - 1, -1, -1):
    #             res[i] *= postfix
    #             postfix *= nums[i]
    #         return res
