class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        Given an integer array nums, return true if any value appears at least twice in the array, and return false
        if every element is distinct.

        Input: nums = [1,2,3,1]
        Output: true

        Input: nums = [1,2,3,4]
        Output: false

        Input: nums = [1,1,1,3,3,4,3,2,4,2]
        Output: true

        Constraints:
        1 <= nums.length <= 10^5
        -10^9 <= nums[i] <= 10^9

        Plan:
        1. Create a nums_set, that will hold values already encountered in the nums array.
        2. Loop through nums, and if nums[i] is in nums_set, then return True. Otherwise, add nums[i] to nums_set.
        3. If we complete the loop without returning false, then we've verified that every value is distinct,
        so return False.
        '''

        nums_set = set()
        for i in range(len(nums)):
            if nums[i] in nums_set:
                return True
            else:
                nums_set.add(nums[i])
        return False
