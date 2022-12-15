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
        1. Create visited_set
        2. Loop through nums, check if nums[i] in visited_set. If it is, then return True. Otherwise, add nums[i] to
        visited_set. If the loop completes, then return False.
        '''

        visited_set = set()
        for i in range(len(nums)):
            if nums[i] in visited_set:
                return True
            else:
                visited_set.add(nums[i])
        return False
