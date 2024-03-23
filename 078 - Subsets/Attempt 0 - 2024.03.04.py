from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        078 - Subsets

        https://leetcode.com/problems/subsets/

        Given an integer array nums of unique elements, return all possible subsets (the power set).

        The solution set must not contain duplicate subsets. Return the solution in any order.

        Example 1:
        Input: nums = [1,2,3]
        Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

        Example 2:
        Input: nums = [0]
        Output: [[],[0]]

        Constraints:
        1 <= nums.length <= 10
        -10 <= nums[i] <= 10
        All the numbers of nums are unique.

        Backtracking
        Create final_arr = []

        Base Case 1: If l >= len(nums), then
        '''
        n = len(nums)
        final_arr = []
        def backtrack(start, cur_list):
            final_arr.append(cur_list[:])
            for j in range(start, n):
                cur_list.append(nums[j])
                backtrack(j+1, cur_list)
                cur_list.pop()
        backtrack(0, [])
        return final_arr



result = Solution()
print(result.subsets([1, 2, 3]))  # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(result.subsets([0]))  # [[],[0]]
