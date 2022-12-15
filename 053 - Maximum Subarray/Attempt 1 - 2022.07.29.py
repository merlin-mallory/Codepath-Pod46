class Solution:
    def maxSubArray(self, nums) -> int:
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

        # Initialize our variables using the first element.
        current_subarray = max_subarray = nums[0]

        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)

        return max_subarray

result = Solution()
print(result.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(result.maxSubArray([1]))
print(result.maxSubArray([5,4,-1,7,8]))
