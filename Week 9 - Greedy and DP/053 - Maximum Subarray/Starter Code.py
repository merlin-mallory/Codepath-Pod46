class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

        A subarray is a contiguous part of an array.

        Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
        Output: 6
        Explanation: [4,-1,2,1] has the largest sum = 6.

        Input: nums = [1]
        Output: 1

        Input: nums = [5,4,-1,7,8]
        Output: 23

        Constraints:
        1 <= nums.length <= 10^5
        -10^4 <= nums[i] <= 10^4
        """

result = Solution()
print(result.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(result.maxSubArray([1]))
print(result.maxSubArray([5,4,-1,7,8]))
