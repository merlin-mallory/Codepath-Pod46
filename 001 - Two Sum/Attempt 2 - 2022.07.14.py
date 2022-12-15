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

        Plan:
        1. Create a mapping_dict. Keys: nums[i], values: index.
        2. Loop through nums. If target-nums[i] in mapping dict, then return [i, mapping_dict.get(target-nums[i]].
        Otherwise, add the iteration to dictionary with key = nums[i] and values = index.
        3. We should never finish looping through the array, because we are guaranteed that an answer exists.
        '''
        import collections
        mapping_dict = collections.defaultdict(int)
        for i in range(len(nums)):
            if target-nums[i] in mapping_dict:
                return [i, mapping_dict.get(target-nums[i])]
            else:
                mapping_dict[nums[i]] = i
                