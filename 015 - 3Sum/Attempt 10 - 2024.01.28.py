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
        1. Sort nums. Create final_arr.
        2. Loop through nums, and grab the left value.
            3. Solve twoSum for the two remaining values, and append the results to final_arr.
        4. Return final_arr
        Edge Cases: None
        Time: O(n^2), Space: O(1)
        """
        nums.sort()
        final_arr = []
        i = 0

        while i < len(nums)-1:
            while i > 0 and nums[i] == nums[i-1] and i < len(nums)-1:
                i += 1
            left_num = nums[i]
            l = i + 1
            r = len(nums)-1
            while l < r:
                threeSum = left_num + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:   # threeSum == 0
                    final_arr.append([left_num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
            i += 1
        return final_arr


result = Solution()
print(result.threeSum([-1,0,1,2,-1,-4]))    # [[-1,-1,2],[-1,0,1]]
print(result.threeSum([0,1,1]))             # []
print(result.threeSum([0,0,0]))             # [[0,0,0]
