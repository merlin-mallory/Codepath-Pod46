from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        198 - House Robber

        https://leetcode.com/problems/house-robber/

        You are a professional robber planning to rob houses along a street. Each house has a certain amount of money
        stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security
        systems connected and it will automatically contact the police if two adjacent houses were broken into on the
        same night.

        Given an integer array nums representing the amount of money of each house, return the maximum amount of money
        you can rob tonight without alerting the police.

        Constraints:
        1 <= nums.length <= 100
        0 <= nums[i] <= 400
        '''

solution = Solution()

print(solution.rob([1,2,3,1]))  # 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

print(solution.rob([2,7,9,3,1]))  # 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

print(solution.rob([2,1,1,2]))  # 4
