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
        -10^9 <= nums[i] <= 10^9a

        Plan 1:
        1. Create nums_set.
        2. Loop through nums, and check if nums[i] is in the set. If it is in the set, then return true. If it isn't
        in the set, then add it to the set.
        3. If the loop completes, then we've confirmed that every value is distinct, so return false.
        4. Time: O(n), Space: O(n)

        Plan 2:
        1. Loop through nums, comparing each value with every other index. If at any point there is a match,
        then return true.
        2. If the loop completes, then we've confirmed that every value is distinct, so return false.
        5. Time: O(n^2), Space: O(1).
        '''
        nums_set = set()
        for i in range(len(nums)):
            if nums[i] in nums_set:
                return True
            else:
                nums_set.add(nums[i])
        return False

