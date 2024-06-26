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

        Plan:
        Backtracking
        Time: O(2^n)
        Space: O(n)
        Edge: None
        '''
        # nums.sort()
        stack = []
        final_arr = []
        def backtrack(i):
            if i == len(nums):
                final_arr.append(stack[:])
                return
            stack.append(nums[i])
            backtrack(i+1)
            stack.pop()
            # while (i < len(nums)-1) and (nums[i] == nums[i+1]):
            #     i += 1
            backtrack(i+1)
        backtrack(0)
        return final_arr

result = Solution()
print(result.subsets([1,2,3]))  # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(result.subsets([0]))      # [[],[0]]
