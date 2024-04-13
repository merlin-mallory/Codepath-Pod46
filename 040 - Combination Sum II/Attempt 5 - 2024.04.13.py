from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        040 - Combination Sum II

        https://leetcode.com/problems/combination-sum-ii/

        Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations
        in candidates where the candidate numbers sum to target.

        Each number in candidates may only be used once in the combination.

        Note: The solution set must not contain duplicate combinations.

        Example 1:
        Input: candidates = [10,1,2,7,6,1,5], target = 8
        Output:
        [[1,1,6], [1,2,5], [1,7], [2,6]]

        Example 2:
        Input: candidates = [2,5,2,1,2], target = 5
        Output:
        [[1,2,2], [5]]

        Constraints:
        1 <= candidates.length <= 100
        1 <= candidates[i] <= 50
        1 <= target <= 30

        Plan:
        Backtracking
        Time: O(2^n)
        Space: O(n)
        Edge: None, but need to handle duplicates
        '''
        candidates.sort()
        stack = []
        final_arr = []
        def backtrack(i, cur_sum):
            if cur_sum == target:
                final_arr.append(stack[:])
                return
            if (cur_sum > target) or (i >= len(candidates)):
                return
            stack.append(candidates[i])
            backtrack(i+1, cur_sum + candidates[i])
            stack.pop()
            while (i < len(candidates)-1) and (candidates[i] == candidates[i+1]):
                i += 1
            backtrack(i+1, cur_sum)
        backtrack(0, 0)
        return final_arr

result = Solution()
print(result.combinationSum2([10,1,2,7,6,1,5],8))   # [[1,1,6], [1,2,5], [1,7], [2,6]]
print(result.combinationSum2([2,5,2,1,2],5))        # [[1,2,2], [5]]
print(result.combinationSum2([10,1,2,7,6,1,5], 8))  # [[1,1,6],[1,2,5],[1,7],[2,6]]
