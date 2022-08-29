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
        1. Create final_arr.
        2. Loop through nums(0, len(nums)-2). nums[i] will be the solo_val
        3. Calculate two sum from i+1 to the end of the list (two pointers strategy). Whenever we find nums[left] +
        nums[right] = solo, and i != j, and i !=k, and j != k, append [solo_val, nums[left], nums[right]] to the
        final_arr.
        4. Return the final_arr.
        """
        # Failed attempt, need to account for duplicates with extra loop
        final_arr = []
        nums.sort()

        for i in range(len(nums)-2):
            solo_val = nums[i]
            j = i + 1
            k = len(nums)-1
            while j < k:
                if i == j:
                    j += 1
                    continue

                elif i == k:
                    k -= 1
                    continue

                elif j == k:
                    j += 1
                    continue

                two_sum = nums[j] + nums[k]
                three_sum = two_sum + solo_val

                if three_sum == 0:
                    final_arr.append([solo_val, nums[j], nums[k]])
                    j += 1
                elif three_sum < 0:
                    j += 1
                elif three_sum > 0:  # three_sum > 0
                    k -= 1
                else:
                    j += 1

        return final_arr
