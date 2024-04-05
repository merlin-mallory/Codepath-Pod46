from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        046 - Permutations

        https://leetcode.com/problems/permutations/

        Given an array nums of distinct integers, return all the possible permutations. You can return the answer in
        any order.

        Example 1:
        Input: nums = [1,2,3]
        Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

        Example 2:
        Input: nums = [0,1]
        Output: [[0,1],[1,0]]

        Example 3:
        Input: nums = [1]
        Output: [[1]]

        Constraints:
        1 <= nums.length <= 6
        -10 <= nums[i] <= 10
        All the integers of nums are unique.

        Plan:
        Time: O(n!)
        Space: O(n)
        Edge: None, but need to handle duplicates
        '''
        stack = []
        final_arr = []
        def backtrack(i):
            if i == len(nums):
                final_arr.append(stack[:])
                return
            for num in nums:
                if num not in stack:
                    stack.append(num)
                    backtrack(i+1)
                    stack.pop()
        backtrack(0)
        return final_arr

result = Solution()
print(result.permute([1,2,3]))  # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(result.permute([0,1]))    # [[0,1],[1,0]]
print(result.permute([1]))      # [[1]]
