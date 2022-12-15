from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        https://leetcode.com/problems/3sum/

        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
        and j != k, and nums[i] + nums[j] + nums[k] == 0.

        Notice that the solution set must not contain duplicate triplets.

        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]
        Explanation:
        nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
        nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
        nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
        The distinct triplets are [-1,0,1] and [-1,-1,2].
        Notice that the order of the output and the order of the triplets does not matter.

        Input: nums = [0,1,1]
        Output: []
        Explanation: The only possible triplet does not sum up to 0.

        Input: nums = [0,0,0]
        Output: [[0,0,0]]
        Explanation: The only possible triplet sums up to 0.

        Constraints:
        3 <= nums.length <= 3000
        -10^5 <= nums[i] <= 10^5

        Plan:
        """
        # Failed attempt.
        nums.sort()
        final_arr = []

        for i in range(len(nums)):
            solo = nums[i]
            if i > 0 and solo == nums[i-1]:
                continue

            left_i = i+1
            right_i = len(nums)-1

            while left_i < right_i:
                left = nums[left_i]
                right = nums[right_i]
                three_sum = solo + left + right
                if three_sum == 0:
                    final_arr.append([solo, left, right])
                    left_i += 1
                    while nums[left_i] == nums[left_i - 1] and left_i < right_i:
                        left_i += 1
                elif three_sum > 0:
                    right_i -= 1
                else:  # three_sum < 0
                    left_i += 1

        return final_arr

result = Solution()
print(result.threeSum([-1,0,1,2,-1,-4]))    # [[-1,-1,2],[-1,0,1]]
print(result.threeSum([0,1,1]))             # []
print(result.threeSum([0,0,0]))             # [[0,0,0]]
