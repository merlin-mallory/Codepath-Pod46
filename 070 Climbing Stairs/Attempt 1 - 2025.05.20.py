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
        '''
        import collections
        memo = collections.defaultdict(int)
        memo[0] = 0
        memo[1] = 1
        memo[2] = 2
        def dfs(n):
            if n in memo: return memo[n]
            left_count = dfs(n-1)
            right_count = dfs(n-2)
            memo[n] = left_count + right_count
            return memo[n]
        return dfs(n)

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
