from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        090 - Subsets II

        https://leetcode.com/problems/subsets-ii/

        Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

        The solution set must not contain duplicate subsets. Return the solution in any order.

        Example 1:
        Input: nums = [1,2,2]
        Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

        Example 2:
        Input: nums = [0]
        Output: [[],[0]]

        Constraints:
        1 <= nums.length <= 10
        -10 <= nums[i] <= 10

        Plan:
        Backtracking
        Time: O(2^n)
        Space: O(n)
        Edge: None
        '''
        nums.sort()
        stack = []
        final_arr = []
        def backtrack(i):
            if i == len(nums):
                final_arr.append(stack[:])
                return
            stack.append(nums[i])
            backtrack(i+1)
            stack.pop()
            while (i < len(nums)-1) and (nums[i] == nums[i+1]):
                i += 1
            backtrack(i+1)
        backtrack(0)
        return final_arr

result = Solution()
print(result.subsetsWithDup([1,2,2]))   # [[1, 2, 2], [1, 2], [1], [2, 2], [2], []]
print(result.subsetsWithDup([0]))       # [[0], []]
print(result.subsetsWithDup([1]))       # [[1], []]
print(result.subsetsWithDup([4,4,4,1,4]))
# [[1, 4, 4, 4, 4], [1, 4, 4, 4], [1, 4, 4], [1, 4], [1], [4, 4, 4, 4], [4, 4, 4], [4, 4], [4], []]
