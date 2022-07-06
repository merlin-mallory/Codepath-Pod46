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

        1. Create a set that will keep track of all the visited values.
        2. Loop through the array, and at each step check if the current value is in the set. If true, then return
        true. Otherwise continue.
        3. If we finish the loop without finding a duplicate, then we can safely return False.
        4. Time: O(N), Space: O(N)
        '''

        visited_set = set()
        for num in nums:
            if num in visited_set:
                return True
            visited_set.add(num)
        return False
