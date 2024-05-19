from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        746 - Min Cost Climbing Stairs

        https://leetcode.com/problems/min-cost-climbing-stairs/

        You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the
        cost, you can either climb one or two steps.

        You can either start from the step with index 0, or the step with index 1.

        Return the minimum cost to reach the top of the floor.

        Constraints:
        2 <= cost.length <= 1000
        0 <= cost[i] <= 999

        Plan:
        Dynamic Programming
        Time:
        '''
        if len(cost) == 2: return min(cost)
        dp = [0] * (len(cost))
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[-2], dp[-1])

solution = Solution()

print(solution.minCostClimbingStairs([10,15,20]))  # 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.

print(solution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))  # 6
# Explanation: You will start at index 0.
#         - Pay 1 and climb two steps to reach index 2.
#         - Pay 1 and climb two steps to reach index 4.
#         - Pay 1 and climb two steps to reach index 6.
#         - Pay 1 and climb one step to reach index 7.
#         - Pay 1 and climb two steps to reach index 9.
#         - Pay 1 and climb one step to reach the top.
#         The total cost is 6.

# Neetcode in-place O(n) time, O(1) space solution
# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         for i in range(len(cost) - 3, -1, -1):
#             cost[i] += min(cost[i + 1], cost[i + 2])
#
#         return min(cost[0], cost[1])

# GPT bottom-up O(n) time, O(1) space solution (can modify inplace)
# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         n = len(cost)
#         # If there are only two steps, return the minimum of starting at either step.
#         if n <= 2:
#             return min(cost)
#
#         # Extend the cost array by one to handle the final step past the last element
#         cost.append(0)
#
#         # Iterate from the second step to the end of the array
#         for i in range(2, n + 1):
#             # Update the cost of reaching the current step
#             cost[i] += min(cost[i - 1], cost[i - 2])
#
#         # The result is in the extended position, which aggregates the final minimum cost
#         return cost[n]

# Leetcode O(n) time, O(1) space solution (can't modify inplace)
# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         down_one = down_two = 0
#         for i in range(2, len(cost) + 1):
#             temp = down_one
#             down_one = min(down_one + cost[i - 1], down_two + cost[i - 2])
#             down_two = temp
#
#         return down_one

# GPT O(n) time, O(n) space (memoization)
# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         memo = {}
#         def min_cost(i):
#             if i in memo:
#                 return memo[i]
#             if i == 0:
#                 return cost[0]
#             if i == 1:
#                 return cost[1]
#             memo[i] = cost[i] + min(min_cost(i - 1), min_cost(i - 2))
#             return memo[i]
#
#         n = len(cost)
#         return min(min_cost(n - 1), min_cost(n - 2))
