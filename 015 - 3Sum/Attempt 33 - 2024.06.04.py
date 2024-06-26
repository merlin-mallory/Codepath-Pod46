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
        Two Pointers
        Time: O(n^2)
        Space: O(1)
        Edge: None, but need to handle duplicates
        """
        nums.sort()
        final_arr = []
        i = 0
        while i < len(nums):
            while (i > 0) and (i < len(nums)-1) and (nums[i] == nums[i-1]):
                i += 1
            left_val = nums[i]
            l, r = i+1, len(nums)-1
            while l < r:
                three_sum = left_val + nums[l] + nums[r]
                if three_sum > 0: r -= 1
                elif three_sum < 0: l += 1
                else:
                    final_arr.append([left_val, nums[l], nums[r]])
                    l += 1
                    while (l < r) and (nums[l] == nums[l-1]):
                        l += 1
            i += 1
        return final_arr

result = Solution()
print(result.threeSum([-1,0,1,2,-1,-4]))    # [[-1,-1,2],[-1,0,1]]
print(result.threeSum([0,1,1]))             # []
print(result.threeSum([0,0,0]))             # [[0,0,0]
print(result.threeSum([-1,0,1,0]))          # [[-1,0,1]]
print(result.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
# [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
print(result.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
# [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
