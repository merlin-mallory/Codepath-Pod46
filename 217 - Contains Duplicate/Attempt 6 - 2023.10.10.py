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

        1. Create nums_set
        2. Loop through nums. If num is in nums_set, then return False. Otherwise, add num to nums_set and continue
        3. Return True
        '''

        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            else:
                nums_set.add(num)

        return False

