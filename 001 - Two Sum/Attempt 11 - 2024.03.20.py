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
        Hashmap
        Create nums_dict. Keys: nums[i], Values: index of keys.
        Loop through nums
            Grab cur, cur_i.
            Calc desired_complement.
            Check if desired_complement is in nums_dict. If so, return [cur_i, nums_dict[desired_complement]].
            Add cur to nums_dict.
        Time: O(n)
        Space: O(n)
        Edge: None
        '''
        import collections
        nums_dict = collections.defaultdict(int)
        for cur_i, cur_v in enumerate(nums):
            desired_complement = target - cur_v
            if desired_complement in nums_dict:
                return [cur_i, nums_dict[desired_complement]]
            nums_dict[cur_v] = cur_i
