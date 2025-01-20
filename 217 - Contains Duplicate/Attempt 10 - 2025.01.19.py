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

        Time: O(n)
        Space: O(n)
        Edge: None

        Alt: sort (O(n log n) time, O(1) space)
        '''
        nums_set = set()
        for num in nums:
            if num in nums_set: return True
            nums_set.add(num)
        return False

