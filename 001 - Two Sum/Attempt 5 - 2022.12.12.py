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

        Constraints:

        2 <= nums.length <= 10^4
        -10^9 <= nums[i] <= 10^9
        -10^9 <= target <= 10^9
        Only one valid answer exists.

        Plan 1:
        1. Loop through nums and compare every index with every other index. If the sum ever equals the target,
        then return those indexes.
        2. Time: O(n^2), Space: O(1).

        Plan 2:
        1. Create a twosum_dict. Keys: target_values, values: the target value's index
        2. Loop through nums. Calculate target-nums[i]. Check if the result is in the hashmap. If the result is in
        the hashmap, then return [i, target_values[target-nums[i]]]. Otherwise, add target[values[target-nums[i]] = i.
        3. Time: O(n), Space: O(n).
        '''
        twosum_dict = {}
        for i in range(len(nums)):
            target_val = target-nums[i]
            if target_val in twosum_dict:
                return [i, twosum_dict[target_val]]
            else:
                twosum_dict[nums[i]] = i

# Test comment
