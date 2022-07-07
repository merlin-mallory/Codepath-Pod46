import collections


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add
        up to target.

        You may assume that each input would have exactly one solution, and you may not use the same element twice.

        You can return the answer in any order.

        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

        Input: nums = [3,2,4], target = 6
        Output: [1,2]

        Input: nums = [3,3], target = 6
        Output: [0,1]

        Plan:
        1. Create a complement_dict (keys: nums[i], values: (complement, index of key)
        2. Loop through nums to create the complement dict.
        3. Loop through the complement dict, and search for a match with the complement. If a match is found,
        then return the matching indexes.

        Constraints:

        '''

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    return [i,j]
