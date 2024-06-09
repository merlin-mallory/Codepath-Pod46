class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        070 - Climbing Stairs

        https://leetcode.com/problems/climbing-stairs/

        You are climbing a staircase. It takes n steps to reach the top.

        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

        Constraints:
        1 <= n <= 45

        Plan:
        Dynamic Programming
        Time: O(n)
        Space: O(n)
        Edge: None
        '''
        if n == 1: return 1
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

solution = Solution()

print(solution.climbStairs(2))  # 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

print(solution.climbStairs(3))  # 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

print(solution.climbStairs(1))  # 1
