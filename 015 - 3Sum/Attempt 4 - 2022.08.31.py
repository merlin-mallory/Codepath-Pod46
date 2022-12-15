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
        1. Sort the array.
        2. Loop from 0 to end of array. Grab the nums[i] value, set this to solo_val.
        3. Calculate twosum between i+1 and the end of the array. Try to find a number where nums[left]+nums[right] =
        - solo_val. This operation goes while left < right, otherwise it breaks, and then outer loop goes to the next
        solo_val. If an answer is found, then add it to the final array, and move the left and right pointers past
        duplicates.
        4. Return the final array.
        """
        nums.sort()
        final_arr = []
        added_set = set()

        def helper(solo_val, nums, left, right):
            while left < right:
                current_val = nums[left] + nums[right]
                if current_val == -solo_val:
                    if (solo_val, nums[left], nums[right]) not in added_set:
                        final_arr.append([solo_val, nums[left], nums[right]])
                        added_set.add((solo_val, nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif current_val < -solo_val:
                    left += 1
                elif current_val > -solo_val:
                    right -= 1

        for i in range(len(nums)):
            solo_val = nums[i]
            helper(solo_val, nums, i+1, len(nums)-1)


        return final_arr

result = Solution()
print(result.threeSum([-1,0,1,2,-1,-4]))
print(result.threeSum([0,1,1]))
print(result.threeSum([0,0,0]))
