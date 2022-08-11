class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/missing-number/

        Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range
        that is missing from the array.

        Input: nums = [3,0,1]
        Output: 2
        Explanation: n = 3 since there are 3 numbers, so all numbers are in the range
        [0,3]. 2 is the missing number in the range since it does not appear in nums.

        Input: nums = [0,1]
        Output: 2
        Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [
        0,2]. 2 is the missing number in the range since it does not appear in nums.

        Input: nums = [9,6,4,2,3,5,7,0,1]
        Output: 8
        Explanation: n = 9 since there are 9 numbers, so all numbers are
        in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

        Constraints:
        n == nums.length
        1 <= n <= 10^4
        0 <= nums[i] <= n
        All the numbers of nums are unique.

        Plan:
        1. Make nums a set.
        2. Check if nums+1 is a set, up to n. When we discover the element not in the set, then return that number.
        3. Check if nums-1 is a set, down to 0. When we discover the element not in the set, then return that number.
        """
        nums_set = set(nums)
        for i in range(len(nums)+1):
            if i not in nums_set:
                return i
