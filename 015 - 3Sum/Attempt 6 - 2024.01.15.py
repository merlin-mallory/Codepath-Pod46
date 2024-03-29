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

        1. Loop through nums once, using nums[i] as left_val, and then solve two sum for right_val.
            2. Check if left_val + right_val == 0. If so, then transform into set. And check if that set is in the
            final_set.
        3. Transform the final_set into an array, and return.
        4. Time complexity: O(n^3), space complexity: O(n^3)
        """
        final_arr = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = a+nums[l]+nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    final_arr.append([a, nums[l], nums[r]])
                    l += 1
                    while (nums[l] == nums[l-1]) and (l < r):
                        l += 1

        return final_arr



result = Solution()
print(result.threeSum([-1,0,1,2,-1,-4]))    # [[-1,-1,2],[-1,0,1]]
print(result.threeSum([0,1,1]))             # []
print(result.threeSum([0,0,0]))             # [[0,0,0]
